"""Queen

Creates the majestic queen bot.

	"All your drones are belong to her".

	Arguments
		None

"""
import time
import communication as comms
import helpers
import multiprocessing

class SwarmState(object):
	"""Swarm State

	Represents the current state of the swarm. Used to make all decisions and must be passed to many methods.

	"""
	pass

def setup(swarm):
	"""Setup

	Perform the Queen swarm setup.

	"""
	# Sleep for 2 seconds
	print 'Sleeping for 2 seconds'
	time.sleep(2)
	# Setup link
	swarm.link = comms.Link(read_timeout=2)
	print 'Link setup'
	now = time.time()
	# Get list of active drones - Blocking
	swarm.drones = helpers.get_active_drones(swarm.link)
	time_taken = time.time() - now
	print 'Recieved drones: %s' % (swarm.drones,)
	print 'Time taken: %s' % (time_taken,)
	# Setup Process pool
	swarm.pool = multiprocessing.Pool(processes=len(swarm.drones))


if __name__ == '__main__':
	# TODO: CLI arguments
	# Startup routine
	print 'Performing Queen startup routine'
	# Create swarm object
	swarm = SwarmState()
	# Perform queen swarm setup
	setup(swarm)
	import pdb; pdb.set_trace()
	# Start heartbeat loop
