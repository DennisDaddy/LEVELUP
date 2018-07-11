import unittest
import os
import json
from app import create_app, db

class CommentTestCase(unittest.TestCase):
    """This is a comment class test"""

    def setUp(self):
        """Define test variables and initialize app"""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.comment = {'title': 'Go to Borabora for vacation'}

        # Binds the app to the current context
        with self.app.app_context():
            # create  tables

            db.create_all()

    def test_comment_creation(self):
        """Test comment creation"""

        res = self.client().post('/level/api/v1/comments/', data=self.comment)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_all_comments(self):
        """Test for getting all comments"""

        res = self.client().post('/level/api/v1/comments/', data=self.comment)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/comments/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Go to Borabora', str(res.data))


    def test_comment_deletion(self):
        """ Test comment deletion """

        rv = self.client().post(
            '/comment/',
            data={'title': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/comments/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/comments/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """ teardown  initialized variables """
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()