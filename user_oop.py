class User(object):
	

	def __init__(self):
		self.users = {}
		

		option = input("Press Yes if Registered or No if you have an account to login ? Yes/No? ")

		if option == "Yes":
			self.log_user()

		elif option == "No":
		    self.register()
	
	def register(self):
		user_enter = input("Enter user name: ")

		if user_enter in self.users:
			print("\nLogin name already exists!\n")
		else:
		    createPassw = input("Create new password: ")
		    self.users[user_enter] = createPassw
		    print("\n User successfully created\n")	

	def log_user(self):
		login = input("Enter user name: ")
		passw = input("Enter password: ")

		if login in self.users and self.users[login] == passw:
			print("\nLogin successfully!\n")
		else:
		    print("\nUser doesn't exists or wrong password!\n")


dennis =User()
dennis.register()
dennis.log_user()