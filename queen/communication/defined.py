

# Defined payloads
defined_payloads = (
	{
		'id': 0,
		'name': 'Discover',
		'parameters': (
			('swarm_name', str),
		)
	},
	{
		'id': 1,
		'name': 'DiscoverResponse',
		'parameters': ()
	},
	{
		'id': 2,
		'name': 'Heartbeat',
		'parameters': ()
	},
	{
		'id': 3,
		'name': 'IdleResponse',
		'parameters': (
			('duration', int),
		)
	},
)

