
class User(object):
	

	def __init__(self):
		self.users = {}
		self.comments = {}
		self.option = ""		

		option = input("Press Yes if Registered or No if you have an account to login ? Yes/No? ")

		if option == "Yes":
			self.log_user()

		elif option == "No":
		    self.register()
		else:
			print("Enter the right value up there to continue ")
			exit()   
		 
	
	def register(self):
		user_enter = input("Enter user name: ")
		first_name = input("Enter first name: ")
		last_name = input("Enter last name: ")
		email = input("Enter your email: ")

		if user_enter in self.users:
			print("\nUser name already exists!\n")
		else:
		    createPassw = input("Create new password: ")
		    self.users[user_enter] = createPassw
		    print("\n User successfully created enter your details below to login\n")	

	def log_user(self):
		login = input("Enter user name: ")
		passw = input("Enter password: ")

		if login in self.users and self.users[login] == passw:
			print("\nLogin successfully!\n")
		else:
		    print("\nUser doesn't exists or you have entered wrong password!\n")

	def add_comment(self):
		if self.log_user:
		    comment_title = input("Enter comment title: ")
		    comment_content = input("Enter comment title: ")
		    self.comments[comment_title] = comment_title
		    self.comments[comment_content] = comment_content
		    print("\nYour comment is successfully created!!\n")
		    print(comment_title)
		    print(comment_title)
		else:
			print("\nLogin first to add comment!\n")

dennis =User()
dennis.register()
dennis.log_user()
dennis.add_comment()