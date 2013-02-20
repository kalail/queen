
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
			'x': (0, 0),
			# Inches
			'y': (1, 0),
			# Inches
			'r': (2, 0),
			# Degrees CW from arena north
			'healthy': (3, False),
			# Whether the drone is working as expected
		}
	},
)
