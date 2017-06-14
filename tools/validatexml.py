import os
import sys
import boto3
import argparse
import re
from collections import Counter
from lxml import etree

guidlibrary = {}

def lists3(outputfolder):
    s3 = boto3.client('s3')

    # Make sure the output folder exists
    if not os.path.isdir(outputfolder):
        os.makedirs(outputfolder)
    else:
        clearfolder(outputfolder)

    projOutputfolder = os.path.join(outputfolder, "ProjectType")
    if not os.path.isdir(projOutputfolder):
        os.makedirs(projOutputfolder)
    else:
        clearfolder(projOutputfolder)

    typeoutputfolder = os.path.join(outputfolder, "ErrorType")
    if not os.path.isdir(typeoutputfolder):
        os.makedirs(typeoutputfolder)
    else:
        clearfolder(typeoutputfolder)



    errorfile = os.path.join(outputfolder, "errors.log")

    paginator = s3.get_paginator('list_objects')

    xsd_doc = etree.parse('../Project/XSD/V1/Project.xsd')
    xsd = etree.XMLSchema(xsd_doc)

    iterator = paginator.paginate(Bucket='sfr-riverscapesdata')
    for page in iterator:
        if 'Contents' in page:
            for line in page['Contents']:
                if re.match(".*/project\.rs\.xml", line['Key']):
                    key = line['Key']
                    print "Found Project {}".format(key)

                    try:
                        XMLFileValidator(key, outputfolder, xsd)
                    except Exception, e:
                        message = str(e)
                        with open(errorfile, 'a+') as f:
                            f.write('PARSE_FAIL: {0}\n    {1}'.format(line['Key'], message))

class ValidatorResult():

    def __init__(self, name, state, errors=[]):
        self.name = name
        self.status = state
        self.errors = errors

class XMLFileValidator():

    def __init__(self, key, outputfolder, xsd):
        s3 = boto3.client('s3')
        self.xsd = xsd
        self.validators = []
        self.key = key
        self.outputfolder = outputfolder
        self.projoutputfolder = os.path.join(outputfolder, "ProjectType")
        self.typeoutputfolder = os.path.join(outputfolder, "ErrorType")

        self.xmlfile = s3.get_object(Bucket="sfr-riverscapesdata", Key=key)['Body'].read()

        self.dom  = etree.fromstring(self.xmlfile)
        self.projtype = self.dom.find('ProjectType').text.strip()

        if self.projtype == "":
            projtype = "Other"

        self.outfile = os.path.join(self.projoutputfolder, '{}.log'.format(self.projtype))
        self.allfile = os.path.join(self.outputfolder, 'Riverscapes.log')

        self.xmlvalidate()
        self.guids()
        self.ids()
        self.paths()

        self.printoutputs()

    def printoutputs(self):
        overallpass = len([v for v in self.validators if v.status == "FAIL"]) == 0
        if overallpass:
            self.printToFile('PASS: {} Checks Passed: {}\n'.format(self.key, str([v.name for v in self.validators])))
        else:
            self.printToFile('FAIL: {} Checks Passed: {}\n'.format(self.key, str([v.name for v in self.validators if v.status == "PASS"])))
            for v in self.validators:
                if v.status == "FAIL":
                    for err in v.errors:
                        self.printToFile('    [{}]: {}\n'.format(v.name, err), v.name)


    def printToFile(self,message, errType=None):
        with open(self.outfile, 'a+') as f, open(self.allfile, 'a+') as ff:
            f.write(message)
            ff.write(message)
        if errType is not None:
            errTypePath = os.path.join(self.typeoutputfolder, "{}.log".format(errType))
            with open(errTypePath, 'a+') as f:
                f.write("{} : {}\n".format(self.key, message.strip()))

    def xmlvalidate(self):
        xsdvalidate = self.xsd.validate(self.dom)
        if xsdvalidate:
            self.validators.append(ValidatorResult("XSD Validation", "PASS"))
        else:
            errors = []
            for err in self.xsd.error_log:
                errors.append("Line:{}  xpath: {} msg: {}  ERR_{}".format(err.line, err.path,
                                                                                err.message, err.type))
            self.validators.append(ValidatorResult("XSD Validation", "FAIL", errors))

    def guids(self):
        """
        Sanity checks on the guids
        :return:
        """
        global guidlibrary
        fileguids = [a.attrib['guid'].upper() for a in self.dom.getroottree().iterfind('//*[@guid]')]
        errors = []
        if len(fileguids) == 0:
            errors.append("No guids found.")
        else:
            # Check for guids that are duplicated
            dupes = [k for k,v in Counter(fileguids).items() if v > 1]
            if len(dupes) > 0:
                errors.append("Duplicate guids inside a single file: {}".format(dupes))

            # Don't do this test unless we have a guid library
            if guidlibrary is not None:
                globerrors = []
                for libkey, libguids in guidlibrary.iteritems():
                    dupes = [g for g in fileguids if g in libguids]
                    if len(dupes) > 0:
                        globerrors.append("Duplicate guid [{1}] found in another file: {0}".format(libkey, dupes))
                # Add these to check later
                guidlibrary[self.key] = fileguids
                if len(globerrors) > 0:
                    self.validators.append(ValidatorResult("Guids Unique Globally", "FAIL", globerrors))
                else:
                    self.validators.append(ValidatorResult("Guids Unique Globally", "PASS"))

        if len(errors) > 0:
            self.validators.append(ValidatorResult("Guids Unique Locally", "FAIL", errors))
        else:
            self.validators.append(ValidatorResult("Guids Unique Locally", "PASS"))

    def ids(self):
        """sanity checks on IDs"""
        errors = []
        ids = [a.attrib['id'] for a in self.dom.getroottree().iterfind('//*[@id]')]
        dupes = [k for k, v in Counter(ids).items() if v > 1]
        if len(dupes) > 0:
            errors.append("Duplicate ids inside a single file: {}".format(dupes))

        if len(errors) > 0:
            self.validators.append(ValidatorResult("Ids Unique Locally", "FAIL", errors))
        else:
            self.validators.append(ValidatorResult("Ids Unique Locally", "PASS"))

    def paths(self):
        pathattrib = [a.attrib['path'].strip() for a in self.dom.getroottree().iterfind('//*[@path]')]
        pathnodes = [a.text.strip() for a in self.dom.getroottree().iterfind('//Path')]
        errors = []
        for p in pathattrib+pathnodes:
            if re.match('^([A-Za-z]:|/)', p):
                errors.append("Invalid absolute path detected: '{}'".format(p))

        if len(errors) > 0:
            self.validators.append(ValidatorResult("Path Checking", "FAIL", errors))
        else:
            self.validators.append(ValidatorResult("Path Checking", "PASS"))

    def internalRefs(self):
        print "internal refs"

    def externalRefs(self):
        print "external refs"


def clearfolder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def main():
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputfolder',
                        type=str,
                        default="validation",
                        help='Write the results of the operation to a specified logfile (optional)')
    args = parser.parse_args()

    try:
        lists3(args.outputfolder)
    except AssertionError as e:
        print "Assertion Error", e
        sys.exit(0)
    except Exception as e:
        print 'Unexpected error: {0}'.format(sys.exc_info()[0]), e
        raise
        sys.exit(0)

"""
This handles the argument parsing and calls our main function
If we're not calling this from the command line then
"""
if __name__ == '__main__':
    main()
