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
		self.new = True


def drone_loop(link, shared, msg):
	print 'Processing drone loop'
	time.sleep(0.2)
	cmd_msg = comms.Message(to_id=6, from_id=1, type_id=5, payload='GARBAGE')
	return link, cmd_msg


def drone_loop_callback(link, msg):
	print 'Sending message from callback'
	link.send_message(msg)

def heartbeat_loop(link, pool, shared):
	# Create waitlist from updated list of active drones
	waitlist = shared.swarm.drones
	# Send heartbeat
	heartbeat = comms.Message(to_id=0, from_id=1, type_id=0, payload='HEARTBEAT')
	link.send_message(heartbeat)
	while True:
		# Wait for msg
		message = link.read_message()
		# Check for timeout
		if not message:
			break
		# extract drone id
		drone_id = message.from_id
		if drone_id in waitlist:
			waitlist.remove(drone_id)
			pool.apply_async(drone_loop, [shared, message], callback=drone_loop_callback)
		if not waitlist:
			break


def queen_loop(link, swarm):
	# Setup Process pool
	print 'Spinning up process pool'
	pool = multiprocessing.Pool(processes=len(swarm.drones))
	print 'Creating shared memory'
	# Setup shared memory
	shared = helpers.setup_shared_memory()
	shared.swarm = swarm
	# Start heartbeat loop
	while True:
		start_time = time.time()
		heartbeat_loop(link, pool, shared)
		time_delta = time.time() - start_time
		# Sleep
		time.sleep(1.0 - time_delta)

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
	print 'Startup complete'
	# Start Queen loop
	queen_loop(link, swarm)
