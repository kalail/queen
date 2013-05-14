

class Drone(object):
	"""Drone

	Virtual representation of a drone bot to help with logic processing.

	"""
	states = [
		'Idle',
			duration
		'Deploying',
			complete
			duration
		'Searching',
			tracking
			duration
		'Relocating'
			duration
		'Attacking',
			distance
			captured
			prey_tracker_state
			duration
		'SearchingNest',
			tracking
			duration
		'Returning',
			tracking
			complete
			duration
		'Delivering',
			duration
		'Disconnected',
			duration
	]

	msg_types = [
		'Discover',
		'DiscoverResponse',
		'Heartbeat',
		'IdleResponse',
		'DeployingResponse',
		'SearchingResponse',
		'TrackingResponse',
		'AttackingResponse',
		'CapturingResponse',
		'ReturningResponse',
		'DeliveringResponse',
		'DisconnectedResponse',
	]

	def __init__(self, drone_id):
		self.id = drone_id
		self.prey_captured = None
		self.target_sight = None
		self.hive_sight = None
