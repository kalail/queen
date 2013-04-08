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


def drone_loop(shared, msg, send_message_queue):
	start_time = time.time()
	print 'Processing drone %s' % msg.from_id
	payload = msg.payload
	params = payload.split(',')
	print 'State ID: %s' % params[0]
	print 'Free Memory: %s' % params[1]
	cmd_msg = comms.Message(to_id=6, from_id=1, type_id=5, payload='GARBAGE')
	send_message_queue.put(cmd_msg)
	# Time process
	time_delta = time.time() - start_time
	print time_delta
	
def heartbeat_loop(link, pool, shared, send_message_queue):
	# Create waitlist from updated list of active drones
	waitlist = list(shared.swarm.drones)
	print 'waitlist: %s' % (waitlist,)
	# Send heartbeat
	print 'Sending heartbeat'
	heartbeat = comms.Message(to_id=0, from_id=1, type_id=1, payload='')
	send_message_queue.put(heartbeat)
	while True:
		# Wait for msg
		message = link.read_message()
		# Check for timeout
		if not message:
			print 'Timeout'
			break
		print 'Recieved %s' % (message,)
		# extract drone id
		drone_id = message.from_id
		if drone_id in waitlist:
			waitlist.remove(drone_id)
			print 'Dispatching routine for drone ID %s' % (drone_id,)
			pool.apply_async(drone_loop, [shared, message, send_message_queue])
		if not waitlist:
			print 'Waitlist empty'
			break

def process_message_queue(link, shared, send_message_queue):
	print 'Started message send process'
	while True:
		msg = send_message_queue.get()
		if not msg:
			print 'Quitting message send process'
			break
		print 'Sending queued message'
		link.send_message(msg)

def main_routine(link, swarm):
	# Setup Process pool
	print 'Spinning up process pool'
	pool = multiprocessing.Pool(len(swarm.drones) + 1, helpers.initialize_worker)
	print 'Creating shared memory'
	# Setup shared memory
	shared, send_message_queue = helpers.setup_shared_memory_and_queue()
	shared.swarm = swarm
	# Create message send process
	send_message_process = multiprocessing.Process(target=process_message_queue, args=[link, shared, send_message_queue])
	send_message_process.start()
	# Start heartbeat loop
	try:
		while True:
			start_time = time.time()
			heartbeat_loop(link, pool, shared, send_message_queue)
			time_delta = time.time() - start_time
			# Time loop
			sleep_for = 1.0 - time_delta
			# Check if need to sleep
			if sleep_for < 0:
				continue
			print 'Sleeping for %s' % (sleep_for,)
			time.sleep(sleep_for)
	except KeyboardInterrupt:
		print 'Caught SIGINT, shutting down'
		# Kill pool
		pool.terminate()
	else:
		# Tell pool to finish
		pool.close()
	finally:
		print 'Shutting down process pool'
		pool.join()
		print 'Shutting down main process'

if __name__ == '__main__':
	# TODO: CLI arguments
	# Startup routine
	print 'Performing Queen setup'
	swarm = SwarmState('TheFirstSwarm')
	# Setup link
	link = comms.Link(read_timeout=2)
	print 'Set up link to swarm'
	# Get list of active drones - Blocking
	print 'Getting list of active drones'
	swarm.drones = helpers.get_active_drones(link)
	print 'Recieved drones: %s' % (swarm.drones,)
	print 'Startup complete'
	# Start Queen routine
	main_routine(link, swarm)
