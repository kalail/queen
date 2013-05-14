

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
	{
		'id': 4,
		'name': 'DeployResponse',
		'parameters': (
			('duration', int),
			('complete', bool),
		)
	},
	{
		'id': 5,
		'name': 'DiscoverResponse',
		'parameters': ()
	},
	{
		'id': 6,
		'name': 'Heartbeat',
		'parameters': ()
	},
	{
		'id': 7,
		'name': 'IdleResponse',
		'parameters': (
			('duration', int),
		)
	},
	{
		'id': 8,
		'name': 'Discover',
		'parameters': (
			('swarm_name', str),
		)
	},
	{
		'id': 9,
		'name': 'DiscoverResponse',
		'parameters': ()
	},
	{
		'id': 10,
		'name': 'Heartbeat',
		'parameters': ()
	},
	{
		'id': 11,
		'name': 'IdleResponse',
		'parameters': (
			('duration', int),
		)
	},
	{
		'id': 12,
		'name': 'SwitchState',
		'parameters': (
			('state', int),
		)
	},
)

