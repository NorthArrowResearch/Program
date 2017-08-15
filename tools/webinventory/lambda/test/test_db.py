from os.path import join, dirname
from dotenv import load_dotenv
import json
import unittest

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from handler import getConnection, lambda_handler

def invokeHelper(url):
    """
    Just a little helper function to parse a url
    :param url:
    :return:
    """
    urlsplit = url.split('?')
    proxy = urlsplit[0]
    params = {}
    if len(urlsplit) > 1:
        for pair in urlsplit[1].split("&"):
            equalsplit = pair.split("=")
            params[equalsplit[0]] = equalsplit[1]


    with open('event.json') as data_file:
        event = json.load(data_file)
    event['queryStringParameters'] = params
    event['pathParameters']['proxy'] = proxy
    return lambda_handler(event, None)

class LambdaInvokeTest(unittest.TestCase):

    def test_mysqlconnect(self):
        conn = getConnection()
        self.assertTrue(True)

    def test_getsites(self):
        """Test we can click OK."""
        response = invokeHelper('layers/sites?name=Area_Bf&t=23&r=34&b=43&l=23')
        self.assertTrue(len(json.loads(response['body'])) > 10)


    def test_getfeature(self):
        """Test we can click OK."""
        response = invokeHelper('feature/CBW05583-009753')
        self.assertTrue(len(json.loads(response['body'])) > 0)


if __name__ == "__main__":
    suite = unittest.makeSuite(LambdaInvokeTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



