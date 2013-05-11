import serial
from xbee import XBee
from .messages import Message


class Link(object):
	"""Link

	Link between the queen and the swarm. It maintains state information and
	implements messaging functionality.

	"""

	drone_addrs = [
		None,
		None,
		'\x00\x02',
		'\x00\x03',
		'\x00\x04',
		'\x00\x05',
		'\x00\x06',
		'\x00\x07',
		'\x00\x08',
		'\x00\x09'
	]

	def __init__(self, callback=None, read_timeout=None, write_timeout=None):
		self.port = serial.Serial('/dev/ttyUSB0', 9600, timeout=read_timeout, writeTimeout=write_timeout)
		if callback:
			self.xbee = XBee(self.port, callback=callback)
			self.api = True
		else:
			self.api = False


	def send_message(self, msg):
		"""Send message

		Transmit a message with given parameters through the link.

		"""
		# Convert message
		string = str(msg)
		# Write serial
		if self.api:
			self.__send_packet(string, msg.to_id)
		else:
			self.__send_string(string)
		

	def __send_string(self, string):
		"""Send String

		Write *string* into the associated port.

		"""
		# Try to write string
		try:
			num_bytes = self.port.write(string)
		# Catch timeout
		except serial.SerialTimeoutException:
			print 'Error: timeout writing to port.'
		# Check if expected number of bytes were written
		else:
			if num_bytes != len(string):
				print 'Error: Mismatch in number of bytes written to port.'

	def __send_packet(self, string, to_id):
		"""Send Packet

		Write *string* into the associated port.

		"""
		# Try to write string
		try:
			addr = self.drone_addrs[to_id]
			self.xbee.tx(dest_addr=addr, data=string)
		# Catch timeout
		except serial.SerialTimeoutException:
			print 'Error: timeout writing to port.'


	def __read_string(self):
		"""Read String - Blocks!

		Reads and returns a string if one is recieved.

		"""
		string = self.port.readline()
		return string

	def read_message(self):
		"""Read Message (for serial mode - Blocks!)

		Parses a string, if recieved, and returns a message.

		"""
		# Get string
		if self.api:
			return None
		else:
			string = self.__read_string()
			# Check for timeout
			if not string:
				return None
			msg = Message(string=string)
			return msg


	def close(self):
		"""Close

		Proper close method. must be called manually.

		"""
		if self.api:
			self.xbee.close()
		self.port.close()