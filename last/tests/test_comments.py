import unittest
import os
import json
from app import create_app, db

class CommentTestCase(unittest.TestCase):
    """This is a class for testing comments"""
    def setUp(self):
        """ defines test variables and initialize the app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.comment = {'title': 'This is my number one blog post'}

        # bind the app to the current context
        with self.app.app_context():
            #create tables
            db.create_all()
    
    def test_comment_creation(self):
        """ Test comment creation"""
        tester = self.client().post('/comments/', data=self.comment)
        self.assertEqual(tester.status_code, 201)
        self.assertIn('This is my', str(tester.data))

    def test_api_can_get_all_comments(self):
        """ Test api can get all comments """
        tester = self.client().post('/comments/', data=self.comment)
        self.assertEqual(tester.status_code, 201)
        tester = self.client().get('/comments/')
        self.assertIn('This is my', str(tester.data))
        
    def test_comment_deletion(self):
        """ Test comment deletion """
        rv = self.client().post(
            '/comments/',
            data={'title': 'This is my'}
        )
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/comments/1')
        self.assertEqual(res.status_code, 200)

        


    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()



if __name__== "__main__":
    unittest.main()