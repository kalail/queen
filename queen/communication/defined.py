

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
		'name': 'SearchingResponse',
		'parameters': (
			('duration', int),
			('tracking', bool),
		)
	},
	{
		'id': 6,
		'name': 'RelocatingResponse',
		'parameters': ()
	},
	{
		'id': 7,
		'name': 'AttackingResponse',
		'parameters': (
			('duration', int),
			('distance', int),
			('captured', bool),
		)
	},
	{
		'id': 8,
		'name': 'SearchingNestResponse',
		'parameters': ()
	},
	{
		'id': 9,
		'name': 'ReturningResponse',
		'parameters': (
			('duration', int),
			('tracking', bool),
			('complete', bool),
		)
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

