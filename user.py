class User(object):
	"""docstring for User"""
	def __init__(self, first_name, last_name, password):
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
		self.full_name = first_name + " " + last_name

class Register(User):
	def sign_up(self):
		first_name = raw_input("Enter first_name :")
		last_name = raw_input("Enter Last Name : ")
		email = raw_input("Enter Email: ")
		password = raw_input("Enter password: ")
		password_confirmation = raw_input("Confirm password: ")
		fullname = first_name + " " + last_name

		print("you are %s and you are successfully registered " %fullname)
class Login(User):
	def log_in(self):
		print ("Enter your details below to Login.")
		name = raw_input("Enter your Name : ")
		email = raw_input("Enter Email: ")	
		print("you are %s and you are successfully logged in " %name)



deno =Register("one", "two", "three")
deno.sign_up()

deno =Login("one", "two", "three")
deno.log_in()