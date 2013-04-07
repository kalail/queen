# OLD
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
