#!/usr/bin/python

import sys
import json
import logging
import re
import os
import urllib2
import boto3
import xml.etree.ElementTree as ET


def lambda_handler(event, context):
    """

    :param event:
    :param context:
    :return:
    """

    s3 = boto3.client('s3')

    paginator = s3.get_paginator('list_objects')

    progxml = ET.parse(urllib2.urlopen(os.environ['PROGRAMXML']))
    products = {}
    iterator = paginator.paginate(Bucket=os.environ['INPUTBUCKET'])
    for page in iterator:
        if 'Contents' in page:
            for line in page['Contents']:
                if re.match(".*/project\.rs\.xml", line['Key']):
                    key = line['Key']
                    logging.info("Found Project: {}".format(key))

                    xmlfile = s3.get_object(Bucket=os.environ['INPUTBUCKET'], Key=key)['Body'].read()
                    dom = ET.fromstring(xmlfile)
                    logging.info("Found: {}".format(key))

                    try:
                        products[key] = {
                            'meta': { node.attrib['name'].strip(): node.text.strip() for node in dom.findall('MetaData/Meta') if node.text is not None}
                        }
                    except Exception, e:
                        logging.error("Error parsing key: {}".format(key))

    # logging.info("Updating the CSV from google sheets.")
    # csvfile = urllib2.urlopen(os.environ['PROGRAMCSV'])

    s3.put_object(Body=json.dumps(products), Bucket='sfr-riverscapesdata', Key='inventory.json')
    s3.put_object(Body=json.dumps(products), Bucket='sfr-riverscapes-status', Key='inventory.json')


if __name__ == "__main__":
    from dotenv import load_dotenv
    from os.path import join, dirname

    logging.basicConfig(level=logging.INFO)
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    response = lambda_handler(None, None)