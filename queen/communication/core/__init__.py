"""Communication Core

Implements lower level communication routines.


Available methods:
	
	send_string

"""


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
		raise NotImplementedError

	def send_message():
		raise NotImplementedError

	def ping():
		raise NotImplementedError
