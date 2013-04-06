
class Drone(object):
	"""Drone

	Virtual representation of a drone bot to help with logic processing.

	"""
	def __init__(self):
		self.position = None
		self.prey_captured = None
		self.target_sight = None
		self.hive_sight = None