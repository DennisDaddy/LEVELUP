class User(object):
	"""docstring for User"""
	def __init__(self, name, email, password):
		
		self.name = name
		self.email = email
		self.password = password	
		self.full_name = name + " " + email

		def print_name(self):
			print (self.full_name)


class Login(User):
	"""docstring for Login"""
	def __init__(self, name, email, password):
		super().__init__(name, email)
		self.name = name
		self.password = password
		self.full_name =name

		def login(self):
			print ("yaay")
signin = Login(("kevin", "kamau", "john")
signin = login()