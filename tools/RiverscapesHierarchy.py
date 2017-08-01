import xml.etree.ElementTree as ET
import xml.dom.minidom
from os import path
import string
import argparse
import sys
import random

sites = []

class hierarchyBuilder():


    def __init__(self, xmlFilePath, writetoFile):

        self.tree = ET.parse(xmlFilePath)
        self.writetoFile = writetoFile
        self.nodRoot = self.tree.getroot()

        self.products = self.nodRoot.findall('Definitions/Products/Product')


        self.treePrint(0, "File Tree \n-------------------------------------", )
        self.traverseFileTree(self.nodRoot.find('Hierarchy'))
        # treePrint(0, "Rave Tree \n-------------------------------------")
        # traverseViewTree(nodRoot.find('ViewTree'))

    def traverseFileTree(self, root,level=0):
        level +=1
        children = root.findall("*")

        for child in children:
            if child.tag == "Collection":
                for col in getCollectionElements(self.nodRoot.find("Definitions/Collections/Collection[@id='{}']".format(child.attrib['ref']))):
                    self.treePrint(level, "/" + str(col))
                    self.traverseFileTree(child, level)

            elif child.tag == "Group":
                grp = self.nodRoot.find("Definitions/Groups/Group[@id='{}']".format(child.attrib['ref']))
                self.treePrint(level, "/" + grp.attrib["folder"])
                self.traverseFileTree(child, level)

            elif child.tag == "Product":
                prod = self.nodRoot.find("Definitions/Products/Product[@id='{}']".format(child.attrib['ref']))
                self.treePrint(level, "/" + prod.attrib["folder"] + "/project.rs.xml")

    def traverseViewTree(self, root, level=0, recurseID=None, newLevel=False):
        level +=1
        children = root.findall("*")

        for child in children:
            if child.tag == "Collection":
                # Louie, I think this is the start of a beautiful recursion
                if 'recurse' in child.attrib:
                    if newLevel is True:
                        for col in getCollectionElements(self.nodRoot.find("Definitions/Collections/Collection[@id='{}']".format(child.attrib['ref'])), recurseID):
                            self.treePrint(level, "+ " + str(col))
                            self.traverseViewTree(child, level, col)
                    else:
                        for col in getCollectionElements(self.nodRoot.find("Definitions/Collections/Collection[@id='{}']".format(child.attrib['ref'])), ""):
                            self.treePrint(level, "+ " + str(col))
                            self.traverseViewTree(child, level, col)
                # Help. I'm recursing and I can't get out
                else:
                    # Either we're a member of the recursing method or we're just filtered by it
                    for col in getCollectionElements(self.nodRoot.find("Definitions/Collections/Collection[@id='{}']".format(child.attrib['ref'])), recurseID):
                        self.treePrint(level, "+ " + str(col))
                        self.traverseViewTree(child, level, recurseID)

            elif child.tag == "Recurse":
                self.traverseViewTree(self.nodRoot.find('ViewTree'), level, recurseID, True)

            elif child.tag == "Group":
                grp = self.nodRoot.find("Definitions/Groups/Group[@id='{}']".format(child.attrib['ref']))
                self.treePrint(level, "+ " + grp.attrib["folder"])
                self.traverseViewTree(child, level, recurseID)

            elif child.tag == "Product":
                prod = self.nodRoot.find("Definitions/Products/Product[@id='{}']".format(child.attrib['ref']))
                self.treePrint(level, "- " + prod.attrib["folder"])


    def treePrint(self, level, name):
        output = level*4*" " + name
        with open(self.writetoFile, "a") as myfile:
            myfile.write(output + "\n")
        print output

def getCollectionElements(collection, recurseParent=None):
    if "pattern" in collection.find("Allow").attrib:
        if collection.attrib['id'] == "COL_YEAR":
            return [2011, 2012, 2013, 2014, 2015]
        elif collection.attrib['id'] == "COL_VISIT":
            sites = []
            for n in range(1):
                sites.append(genVisit())
            return sites
        elif collection.attrib['id'] == "COL_SITE":
            sites = []
            for n in range(4):
                sites.append(genSite())
            return sites
        elif collection.attrib['id'] == "COL_FLOW":
            sites = []
            for n in range(4):
                sites.append(genFlow())
            return sites
    else:
        if recurseParent is not None:
            return [m.attrib['folder'] for m in collection.findall("Member") if "recurseParent" not in m.attrib or m.attrib['recurseParent']==recurseParent]
        else:
            return [m.attrib['folder'] for m in collection.findall("Allow")]

    return []

def genSite():
    """
    Generate dummy sites
    :return:
    """
    first = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    second = '000000-'
    third   = ''.join(random.choice(string.digits) for _ in range(5))
    return "{}{}{}".format(first,second,third)

def genFlow():
    """
    Generate dummy sites
    :return:
    """
    second = '0000'
    third   = ''.join(random.choice(string.digits) for _ in range(5))
    return "{}{}{}".format(random.choice(['M','S']),second,third)

def genVisit():
    """
    Generate dummy sites
    :return:
    """
    return "{}_{}".format("VISIT",''.join(random.choice(string.digits) for _ in range(4)))

def main():
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', type=argparse.FileType('r'))
    parser.add_argument('--outputfile',
                        type=str,
                        default="validation",
                        help='Write the results of the operation to a specified logfile (optional)')
    args = parser.parse_args()

    try:
        hierarchyBuilder(args.inputfile.name, args.outputfile)
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
