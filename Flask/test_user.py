from user import app
import unittest 
from flask import url_for, session
import os

class FlaskTestCase(unittest.TestCase):

	# Test that flask was set up correctly
	def test_index(self):
		tester = app.test_client(self)
		response =tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)
	def test_incorrect_login():
		response = self.client.post('login',
			data= dict(username="", pasword=""),
			follow_redirects=True)

	def test_homepage():
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)	
if __name__ == '__main__':
			unittest.main()		