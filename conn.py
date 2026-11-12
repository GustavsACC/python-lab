class DatabaseConnection:
	def __init__(self, port, hostname, username, password):
		self.port = port
		self.hostname = hostname
		self.username = username
		self.password = password

	def show_parameters(self):
		print(f"Port: {self.port}")
		print(f"Hostname: {self.hostname}")
		print(f"Username: {self.username}")
		print(f"Password: {self.password}")


connection = DatabaseConnection(
	port="<PORT>",
	hostname="<HOSTNAME>",
	username="<USERNAME>",
	password="<PASSWORD>",
)
connection.show_parameters()
