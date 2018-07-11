import unittest
import os
import json
from app import create_app, db

class CommentTestCase(unittest.TestCase):
    """ This is class for testing comments """
    def setUp(self):
        """ Define test variables and initializ the app """
        
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.comment = {'title': 'This is my first  title' }

        # bind the app

        with self.app.app_context():

            # create tables
            db.create_all()
    
    def test_comment_creation(self):
        """ Test comment creation by post request """

        res = self.client().post('/comments/, data=self.comment')
        self.assertEqual(res.status_code, 201)
        self.assertIn('This is my', str(res.data))

        def tearDown(self):
            """ teardown initialized variables """
            with self.app.app_context():

                # drop all tables
                db.session.remove()
                db.drop_all()


if __name__ == "__main__":
    unittest.main()
