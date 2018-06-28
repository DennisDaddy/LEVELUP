class User(object):
	"""docstring for User"""
	def register(self):
		print ("Welcome to commandline App enter your details below to Register")
		first_name = input("Enter your first name :")
		last_name = input("Enter your Last Name : ")
		user_name = input("Enter your user Name : ")
		email = input("Enter your Email: ")
		password = input("Enter your password: ")
		password_confirmation = input("Confirm password: ")
		fullname = first_name + " " + last_name

		print("you are %s and you are successfully registered " %fullname)

	def login(self):
		print ("Enter your details below to Login.")
		user_name = input("Enter your user Name : ")
		email = input("Enter Email: ")	
		print("you are %s and you are successfully logged in " %user_name)


deno =User()
deno.register()
deno.login()

