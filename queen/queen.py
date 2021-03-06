"""Queen

Creates the majestic queen bot.

	"All your drones are belong to her".

	Arguments
		None

"""
import time
import communication
import helpers
import multiprocessing
import routines


class Swarm(object):
	"""Swarm

	Represents the current state of the swarm. Used to make decisions and must be passed to any method making them.

	"""
	
	def __init__(self, name):
		self.name = name
		self.drone_ids = range(2,10)
		self.active_drone_ids = []
		self.drones = []


def drone_loop(swarm, msg, message_queue):
	print 'Processing drone ID %s' % msg.from_id
	start_time = time.time()
	# Extract payload
	payload = msg.payload
	# params = payload.split(',')
	print payload
	# Update swarm
	# swarm_key = 'drone_%s' % msg.from_id
	# swarm[swarm_key] = params[0]
	# print 'State ID: %s' % params[0]
	# print 'Free Memory: %s' % params[1]
	# # Simulate msg to drone
	# sim_msg = comms.Message(to_id=6, from_id=1, type_id=5, payload='GARBAGE')
	# message_queue.put(sim_msg)
	# Time process
	time_delta = time.time() - start_time
	print 'Drone ID %s processed in %s seconds' % (msg.from_id, time_delta)


def heartbeat_loop(link, pool, swarm, message_queue):
	print 'Starting heartbeat loop'
	# Create waitlist from updated list of active drones
	waitlist = list(swarm['active_drones'])
	print 'Drone waitlist: %s' % (waitlist,)
	# Send heartbeat
	print 'Sending heartbeat'
	heartbeat = communication.Message(to_id=0, from_id=1, type_id=1, payload='')
	message_queue.put(heartbeat)
	while True:
		# Wait for msg
		message = link.read_message()
		# Check for timeout
		if not message:
			print 'Timeout reading heartbeat response'
			break
		print 'Recieved %s' % (message,)
		# extract drone id
		drone_id = message.from_id
		if drone_id in waitlist:
			waitlist.remove(drone_id)
			# Process msg in drone_loop - Async
			pool.apply_async(drone_loop, [swarm, message, message_queue])
		if not waitlist:
			print 'All drones responded'
			break


def process_message_queue(link, message_queue):
	print 'Started message sender'
	while True:
		try:
			msg = message_queue.get(timeout=6)
		except Exception:
			# Catch timeout and repeat
			print 'Timeout in message sender'
			continue
		if not msg:
			print 'Quitting message send process'
			break
		print 'Recieved queued msg %s' % msg
		link.send_message(msg)
		print 'Sent' 


if __name__ == '__main__':
	print 'Starting Queen'
	swarm = Swarm('TheFirstSwarm')
	link = communication.Link(callback=helpers.dummy_callback, read_timeout=2, write_timeout=2)

	try:
		# Discover drones
		print 'Discovering active drones'
		for i in xrange(6):
			print 'iteration %s' % i
			routines.discover_drones(link, swarm)
		print 'Starting with drones: %s' % swarm.active_drone_ids

		# Heartbeat loop
		print 'Starting heartbeat loop'
		while True:
			routines.heartbeat_routine(link, swarm)
			print ''

	# Catch interrupt
	except KeyboardInterrupt:
		print '\nCaught SIGINT, shutting down\n'
		link.close()
	else:
		pass

	# # Setup Process pool
	# print 'Spinning up process pool'
	# pool = multiprocessing.Pool(len(swarm.active_drones) + 1, helpers.initialize_worker)
	# # Setup shared memory
	# print 'Creating shared memory'
	# # Create memory manager process
	# memory_manager = multiprocessing.Manager()
	# # Create shared objects
	# shared = memory_manager.dict()
	# message_queue = memory_manager.Queue()
	# shared['swarm'] = swarm.active_drones
	# # Start message sender
	# pool.apply_async(process_message_queue, args=(link, message_queue))
	# time.sleep(2)
	# # Start heartbeat loop
	# try:
	# 	while True:
	# 		start_time = time.time()
	# 		heartbeat_loop(link, pool, swarm, message_queue)
	# 		time_delta = time.time() - start_time
	# 		# Time loop
	# 		sleep_time = 1.0 - time_delta
	# 		# Check if need to sleep
	# 		if sleep_time < 0:
	# 			continue
	# 		print 'Sleeping for %s' % (sleep_time,)
	# 		time.sleep(sleep_time)
	# except KeyboardInterrupt:
	# 	print 'Caught SIGINT, shutting down'
	# 	# Kill pool
	# 	pool.terminate()
	# else:
	# 	# Tell pool to finish
	# 	pool.close()
	# finally:
	# 	print 'Shutting down process pool'
	# 	pool.join()
	# 	print 'Shutting down main process'
