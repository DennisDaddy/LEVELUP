class User(object):
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name

	def all_names(self):
		name = raw_input("Enter you name:")

		print "Your are %s " %name

coolins = User("kimani", "john")
coolins.all_names()		