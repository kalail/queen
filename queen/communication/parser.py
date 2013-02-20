
import queen.settings as settings


class Parser(object):
	"""Parser

	Take a dictionary of parameters and return an object that can parse a string respectively.

	Parameters are of the form:

		'name': (index, example)

	"""

	def __init__(self, msg_id, name, parameters):
		self.msg_id = msg_id
		self.name = name
		self.parameters = parameters

	def __repr__(self):
		return 'Parser for %s message' % self.name


	def parse(self, msg_string):
		"""Return a dictionary containing the message parsed according to class parameters."""

		# Extract values from message string
		param_values = self.__extract_values__(msg_string)

		if len(param_values) != len(self.parameters.keys()):
			print 'Error: Message contained unexpected number of parameter values'
			return None
		# Create parsed message dictionary
		parsed_msg = {}
		# Add individual parameter values
		for key in self.parameters.keys():
			# Create parameter default value
			parsed_msg[key] = None
			# Get parameter descriptors
			descriptors = self.parameters[key]
			var_index = descriptors[0]
			var_example = descriptors[1]
			# Try to cast and save value
			try:
				value = type(var_example)(param_values[var_index]) if type(var_example) != bool else bool(int(param_values[var_index]))
				parsed_msg[key] = value
			except ValueError:
				print 'error parsing value to parameter type'
		# Return parsed message dictionary
		return parsed_msg


	def compose(self, msg_vars):
		"""Return a string containing the given message variables."""

		# Make sure keys are the same
		keys = msg_vars.keys()
		if False in [key in self.parameters.keys() for key in keys]:
			print 'Error: Message contained incorrect parameter values'
			return None

		# Create list of values cast to appropriate strings
		msg_strings = []
		for key in keys:
			value = msg_vars[key]
			msg_strings.append(str(value) if type(value) != bool else str(int(value)))

		# Join values adn return
		msg_string = ';'.join(msg_strings)
		return msg_string


	def __extract_values__(self, msg_string):
		"""Split the values in the message string using the delimiter."""
		delimiter = settings.PACKET_STRUCTURE['MSG_DELIMETER']
		values = msg_string.split(delimiter)
		return values
