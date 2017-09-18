import json
import unittest
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from handler import lambda_handler

class LambdaInvokeTest(unittest.TestCase):

    def test_getsites(self):
        """Test we can click OK."""
        response = lambda_handler(None, None)
        self.assertTrue(len(json.loads(response['body'])) > 10)


if __name__ == "__main__":
    suite = unittest.makeSuite(LambdaInvokeTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



