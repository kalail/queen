"""Communication

Handles all communication between the queen and drones using high level
interfaces.

"""
from .link import Link
from .messages import Message

def setup_comms():
	"""Setup Comms

	Creates and returns a communication handler.
	"""

	new_link = Link()
	return new_link

