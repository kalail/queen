class Message(object):
	"""Message

	Base message object with a 'to' and 'from' field.

	"""
	def __init__(self, string):
		self.string = string
		# Get to field
		self.to_id = self.string[0:1]
		# Get from field
		self.from_id = self.string[1:2]

	def __repr__(self):
		return 'MSG'
		

messages = (
	{
		# 0
		'name': 'CreateLink',
		'parameters': {
			'startup_delay': (0, 1),
			# Seconds
		}
	},
	{
		# 1
		'name': 'CreateLinkResponse',
		'parameters': {
		}
	},
	{
		# 2
		'name': 'Heartbeat',
		'parameters': {
		}
	},
	{
		# 3
		'name': 'HeartbeatResponse',
		'parameters': {
			'x': (0, float),
			# Inches
			'y': (1, float),
			# Inches
			'r': (2, float),
			# Degrees CW from arena north
			'healthy': (3, False),
			# Whether the drone is working as expected
		}
	},
)

