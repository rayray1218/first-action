import random
import unittest
from app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_addition(self):
    	num1 = random.randint(0, 100)
    	num2 = random.randint(0, 100)
    	response = self.app.post('/', data={'num1': str(num1), 'num2': str(num2)})
    	self.assertEqual(response.status_code, 200)
    	self.assertIn(str(num1 + num2).encode(), response.data)

if __name__ == '__main__':
    unittest.main()