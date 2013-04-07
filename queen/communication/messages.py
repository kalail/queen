import re

class Message(object):
	"""Message

	Base message object with a 'to' and 'from' field.

	"""
	def __init__(self, string=None, **kwargs):
		"""Initializer

		Create or parse a message object given a string or msg parameters.

		"""
		# Parse if given string
		if string:
			kwargs = self.__parse(string)
		# Parse Keywords
		self.to_id = int(kwargs['to_id'])
		self.from_id = int(kwargs['from_id'])
		self.type_id = int(kwargs['type_id'])
		self.payload = str(kwargs['payload'])

	def __parse(self, string):
		"""Return a dictionary containing the message parsed according to class parameters."""

		# Create regex and parse string
		# pattern = r'^(?P<to_id>[0-9]+);(?P<from_id>[0-9]+);(?P<type_id>[0-9]+);(?P<payload>.*)\n$'
		regex = re.compile(r'^(?P<to_id>[0-9]+);(?P<from_id>[0-9]+);(?P<type_id>[0-9]+);(?P<payload>.*)\n$')
		match = regex.search(string)
		# Check for parse error
		if not match:
			raise Exception('Could not parse msg')
		# Create parsed dict
		parsed = match.groupdict()
		return parsed

	def __str__(self):
		string = '%s;%s;%s;%s\n' % (self.to_id, self.from_id, self.type_id, self.payload)
		return string

# messages = (
# 	{
# 		# 0
# 		'name': 'CreateLink',
# 		'parameters': {
# 			'startup_delay': (0, 1),
# 			# Seconds
# 		}
# 	},
# 	{
# 		# 1
# 		'name': 'CreateLinkResponse',
# 		'parameters': {
# 		}
# 	},
# 	{
# 		# 2
# 		'name': 'Heartbeat',
# 		'parameters': {
# 		}
# 	},
# 	{
# 		# 3
# 		'name': 'HeartbeatResponse',
# 		'parameters': {
# 			'x': (0, float),
# 			# Inches
# 			'y': (1, float),
# 			# Inches
# 			'r': (2, float),
# 			# Degrees CW from arena north
# 			'healthy': (3, False),
# 			# Whether the drone is working as expected
# 		}
# 	},
# )

