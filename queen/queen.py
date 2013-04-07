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

	Represents the current state of the swarm. Used to make decisions and must be passed to any method making them.

	"""
	
	def __init__(self, name):
		self.name = name
		self.drones = []


if __name__ == '__main__':
	# TODO: CLI arguments
	# Startup routine
	print 'Performing Queen setup'
	swarm = SwarmState('The First Swarm')
	# Sleep for 2 seconds
	print 'Sleeping for 2 seconds'
	time.sleep(2)
	# Setup link
	link = comms.Link(read_timeout=2)
	print 'Set up link to swarm'
	# Get list of active drones - Blocking
	print 'Getting list of active drones'
	swarm.drones = helpers.get_active_drones(link)
	print 'Recieved drones: %s' % (swarm.drones,)
	# Setup Process pool
	print 'Spinning up process pool'
	pool = multiprocessing.Pool(processes=len(swarm.drones))
	print 'Setup complete'
	# Start heartbeat loop
	