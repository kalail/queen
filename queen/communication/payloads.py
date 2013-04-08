import re

class Payload(object):
	"""Payload

	Actual msg object.

	Attributes
		parameters

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

# Defined payloads
defined_payloads = (
	{
		'id': 0,
		'name': 'Initialize',
		'parameters': {
			'swarm_name': (str, 0),
		}
	},
	{
		'id': 1,
		'name': 'Heartbeat',
		'parameters': {
		}
	},
	{
		'id': 2,
		'name': 'Heartbeat',
		'parameters': {
			'state': (int, 0),
			'free_memory': (int, 1),
		}
	},
)

