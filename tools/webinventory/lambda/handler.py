#!/usr/bin/python
import sys
import json
import logging
import pymysql
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def getConnection():
    try:
        conn = pymysql.connect(os.environ['DB_ENDPOINT'],
                               user=os.environ['DB_USERNAME'],
                               passwd=os.environ['DB_PASSWORD'],
                               db=os.environ['DB_NAME'],
                               connect_timeout=5)
        logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
        return conn
    except Exception, e:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

def lambda_handler(event, context):
    """
    This function inserts content into mysql RDS instance
    """
    item_count = 0
    out = {}
    out['headers'] = {
        "X-Requested-With": '*',
        "Access-Control-Allow-Headers": 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with',
        "Access-Control-Allow-Origin": '*',
        "Access-Control-Allow-Methods": 'GET,OPTIONS'
    }


    params = event['queryStringParameters']
    proxy = event['pathParameters']['proxy'].split('/')

    if proxy[0] == 'layers':
        with getConnection().cursor(pymysql.cursors.DictCursor) as cur:
            numrows = cur.execute("""
                SELECT DisplayLabel, WebID, D.Title AS AttributeTitle, AttValue AS AttributeValue
                FROM Features F
                    INNER JOIN Attributes A ON F.FeatureID = A.FeatureID
                    INNER JOIN Layers L ON F.LayerID = L.LayerID
                    INNER JOIN AttributeDefs D ON A.AttributeID = D.AttributeID
                WHERE
                    (L.Title = '{0}')
                    AND (D.Title = '{1}')                    
                """.format(proxy[1], params['name']))
            out['statusCode'] = 200
            resp = cur.fetchall()
            bodyraw = {}
            # Re-map everything by WebID
            for row in resp:
                webid = row['WebID']
                if webid not in bodyraw:
                    bodyraw[webid] = { "DisplayLabel": row['DisplayLabel'] }
                bodyraw[webid][row['AttributeTitle']] = row['AttributeValue']
            out['body'] = json.dumps(bodyraw)
            return out

    #                     AND (F.Top <= {2})
    #                 AND (F.`Left` >= {3})
    #                 AND (F.`Right` <= {4})
    #                 AND (F.Bottom >= {5})

    elif proxy[0] == 'feature':
        with getConnection().cursor(pymysql.cursors.DictCursor) as cur:
            numrows = cur.execute("""
                    SELECT D.Title AS AttributeTitle, AttValue AS AttributeValue
                    FROM Features F
                        INNER JOIN Attributes A ON F.FeatureID = A.FeatureID
                        INNER JOIN AttributeDefs D ON A.AttributeID = D.AttributeID
                    WHERE
                        F.WebID = '{}';
                """.format(proxy[1]))
            out['statusCode'] = 200
            resp = cur.fetchall()
            bodyraw = {}
            bodyraw[proxy[1]] = {}
            # Re-map everything by WebID
            for row in resp:
                bodyraw[proxy[1]][row['AttributeTitle']] = row['AttributeValue']
            out['body'] = json.dumps(bodyraw)
            return out

    else:
        return {
            'statusCode': 400,
            'body': 'PEBKAC ERROR: Problem exists between keyboard and chair.'
        }
