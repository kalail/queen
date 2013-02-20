import queen.settings as settings
import serial

from .parser import Parser
from .codec import Codec, Packet


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

	def __init__(self, communication, drone_id):
		self.id = drone_id
		self.active = False
		self.communication = communication

	
	# params = {
	# 	'startup_delay': 10,
	# }
	def send_message(self, msg_name, params):
		"""Send message

		Transmit a message with given parameters through the link.

		e.g.

			send_message('CreateLink', {
					'startup_delay': 10
				}
			)

		"""
		comms = self.communication
		# Create message
		p = comms.get_parser(msg_name)
		msg_string = p.compose(params)
		# Create packet
		packet = Packet(self.id, settings.QUEEN_ID, p.msg_id, msg_string)
		c = comms.codec
		packet_string = c.encode(packet)
		# Write serial
		self.write(packet_string)
		

	def write(self, string):
		"""Write

		Write *string* into the associated comms module serial port.

		"""
		comms = self.communication
		port = comms.serial
		try:
			num_bytes = port.write(string)

		except serial.SerialTimeoutException:
			print 'Error: timeout in link.write'

		else:
			# Check if expected number of bytes were written
			if num_bytes == len(string):
				return
		
		# Rescue link if timeout or incorrect number of bytes written.
		self.rescue()
		self.write(string)


	def read(self):
		# INCOMPLETE
		comms = self.communication
		port = comms.serial
		try:
			port.readline(eol=settings.PACKET_STRUCTURE['TERMINATOR'])
		except serial.SerialTimeoutException:
			pass


	def rescue(self):
		self.communication.reset_serial()


	def ping(self):
		raise NotImplementedError

	def teardown(self):
		pass
