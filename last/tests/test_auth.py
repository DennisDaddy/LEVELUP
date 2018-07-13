import unittest
import os
import json
from app import create_app, db
class AuthTestCase(unittest.TestCase):
    """Test for authentification blueprint"""

    def setUp(self):
        """Set the the variables"""
        self.app = create_app(config_name="testing")
        # Initialize the test client
        self.client = self.app.test_client

        # user json test data with email and passowrd
        self.user_data = {
            'email': 'test@example.com',
            'password': 'test_password'
        }

        with self.app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()
    

    def test_registration(self):
        """ Test user registration """
        tester = self.client().post('/auth/register', data=self.user_data)
        # get the results in json format
        result = json.loads(res.data.decode())

        self.assertEqual(result['message'], "You are successfully registered")
        self.assertEqual(tester.status_code, 201)

    
    def test_already_registered_user(self):
        """Test that a user cannot register many times """
        tester = self.client().post('/auth/register', data=self.user_data)
        self.assertEqual(tester.status_code, 201)
        second_tester = self.client().post('/auth/register', data=self.user_data)
        self.assertEqual(second_tester.status_code, 202)

        # Get the results in json format
        result = json.loads(second_tester.data.decode())
        self.assertEqual(
            result['message'], "User already exists. Please login.")
        

