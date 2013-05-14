import re

class Message(object):
	"""Message

	Basic message communication object.

	Attributes
		-to_id
		-from_id
		-type_id
		-payload

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
