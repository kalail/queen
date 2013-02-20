class Link(object):
	"""Link

	A link between the queen and a drone. It maintains state information and
	implements messaging functionality.


	Available methods:

		send_message(msg, drone_id)
		Sends a string *msg* to drone with id *drone_id*.
		Returns ``True`` if the message is successfully delivered.

		ping(drone_id)
		Attepts to ping the drone with id *drone_id*.
		Returns ``True`` if the drone is available.

	"""

	def __init__(self, drone_id):
		self.id = drone_id
		self.active = False
		self.create_link

	def send_message(self):
		raise NotImplementedError

	def ping(self):
		raise NotImplementedError

	def teardown(self):
		pass
