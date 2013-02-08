"""Communication

Handles all communication between the queen and drones using high level
interfaces.


Available methods:

	setup_link(drone_id)
	Set up an active connection with drone with id *drone_id*.
	Returns ``True`` if the connection is made.

"""

# import RPi.GPIO
import core

def setup_link(drone_id):
	raise NotImplementedError
	new_link = core.Link(drone_id)
	return new_link