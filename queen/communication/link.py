import serial
from .messages import Message


class Link(object):
	"""Link

	Link between the queen and the swarm. It maintains state information and
	implements messaging functionality.

	"""

	def __init__(self, read_timeout=None, write_timeout=None):
		self.port = serial.Serial('/dev/ttyUSB0', 9600, timeout=read_timeout, writeTimeout=write_timeout)
		self.active = True


	def send_message(self, msg):
		"""Send message

		Transmit a message with given parameters through the link.

		"""
		# Convert message
		string = str(msg)
		# Write serial
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


	def __read_string(self):
		"""Read String - Blocks!

		Reads and returns a string if one is recieved.

		"""
		string = self.port.readline()
		return string


	def read_message(self):
		"""Read Message - Blocks!

		Parses a string, if recieved, and returns a message.

		"""
		# Get string
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
		self.port.close()
		del self.port
		self.active = False


	def __del__(self):
		"""Memory Destructor - Not always called"""

		self.close()