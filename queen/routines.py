import communication
import time
import helpers
import communication.parser as parser

class DiscoverDronesRoutine(object):

	def __init__(self, active_drone_ids):
		self.active_drone_ids = active_drone_ids

	def recieve_response(self, data):
		drone_id = helpers.to_int(data['source_addr'])
		if drone_id not in self.active_drone_ids:
			self.active_drone_ids.append(drone_id)
			print 'Discovered drone with ID: %s' % drone_id
		else:
			print 'Rediscovered drone with ID: %s' % drone_id
		string = data['rf_data']

def discover_drones(link, swarm):
	routine = DiscoverDronesRoutine(swarm.active_drone_ids)
	messages = [communication.Message(to_id=i, from_id=1, type_id=0, payload=swarm.name) for i in swarm.drone_ids if i not in swarm.active_drone_ids]
	link.set_callback(routine.recieve_response)
	for msg in messages:
		link.send_message(msg)
	time.sleep(0.5)
	swarm.active_drone_ids = routine.active_drone_ids


class HeartbeatRoutine(object):

	def __init__(self, link, active_drone_ids):
		self.active_drone_ids = active_drone_ids
		self.drones_responded = []
		self.complete = False
		self.link = link

	def recieve_response(self, data):
		drone_id = helpers.to_int(data['source_addr'])
		if drone_id not in self.active_drone_ids:
			print 'Unexpected response from inactive Drone %s' % drone_id
			return
		if drone_id in self.drones_responded:
			print 'Drone %s responded more than once' % drone_id
			return
		print 'Recieved response from Drone %s' % drone_id
		self.drones_responded.append(drone_id)
		string = data['rf_data']
		msg = communication.Message(string)
		params = parser.parse(msg)
		# Cases
		if msg.type_id == 3:
			print 'Duration in state: %s' % (params['duration'],)
			if params['duration'] > 10:
				order = communication.Message(to_id=drone_id, from_id=1, type_id=12, payload='1')
				self.link.send_message(order)
				print "ERMAGAUD!ERMAGAUD!ERMAGAUD!"
		elif msg.type_id == 4:
			print 'In state "Deploy"\nDuration: %s\nComplete: %s' % (params['duration'], params['complete'])
			if params['complete']:
				order = communication.Message(to_id=drone_id, from_id=1, type_id=12, payload='2')
				self.link.send_message(order)
				print "ERMAGAUD!ERMAGAUD!ERMAGAUD!"
		elif msg.type_id == 5:
			print 'In state "Searching"\nDuration: %s\nTracking: %s' % (params['duration'], params['tracking'])

		check = [i in self.drones_responded for i in self.active_drone_ids]
		if False not in check:
			print 'Routine complete'
			self.complete = True


def heartbeat_routine(link, swarm):
	print 'Sending heartbeat'
	routine = HeartbeatRoutine(link, swarm.active_drone_ids)
	link.set_callback(routine.recieve_response)
	messages = [communication.Message(to_id=i, from_id=1, type_id=2, payload='') for i in swarm.active_drone_ids]
	for msg in messages:
		link.send_message(msg)
	# Try to check if complete in 1 second
	time.sleep(0.5)
	if routine.complete:
		print 'Loop complete'
		return
	time.sleep(0.5)
	if routine.complete:
		print 'Loop complete'
		return
	time.sleep(0.5)
	if routine.complete:
		print 'Loop complete'
		return
	time.sleep(0.5)