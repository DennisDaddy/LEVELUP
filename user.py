class User(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name

	def register(self):
	    first_name = raw_input("Enter Your First name:")
	    last_name = raw_input("Enter Your Last name:")
	    password = raw_input("Enter Your password:")
	    password_confirmation = raw_input("Confirm your password:")
	    all_names = first_name + " " + last_name
	    print "Your are  %s and you are successfullfy registered" %all_names

	def login(self):
			name = raw_input("Enter Your User name:")
			password = raw_input("Enter Your Password:")

			print "Your name is %s and you are successfullfy logged in " %name


coolins = User("kimani", "john")
coolins.register()
coolins.login()		