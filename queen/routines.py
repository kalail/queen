import communication
import time
from communication.messages import Message
import helpers


class DiscoverDronesRoutine(object):

	def __init__(self, active_drone_ids):
		self.active_drone_ids = active_drone_ids

	def recieve_response(self, data):
		drone_id = helpers.to_int(data['source_addr'])
		if drone_id not in self.active_drone_ids:
			self.active_drone_ids.append(drone_id)
			print 'Discovered drone with ID: %s' % drone_id
		string = data['rf_data']

def discover_drones(swarm):
	routine = DiscoverDronesRoutine(swarm.active_drone_ids)
	messages = [communication.Message(to_id=i, from_id=1, type_id=0, payload=swarm.name) for i in swarm.drone_ids if i not in swarm.active_drone_ids]
	print messages[0]
	link = communication.Link(callback=routine.recieve_response, read_timeout=2, write_timeout=2)
	for msg in messages:
		link.send_message(msg)
	time.sleep(1)
	swarm.active_drone_ids = routine.active_drone_ids
	link.close()


class HeartbeatRoutine(object):

	def __init__(self, active_drone_ids):
		self.active_drone_ids = active_drone_ids
		self.drones_responded = []
		self.complete = False

	def recieve_response(self, data):
		drone_id = data['source_addr']
		if drone_id not in self.active_drone_ids:
			print 'Unexpected response from inactive Drone %s' % drone_id
			return
		if drone_id in self.drones_responded:
			print 'Drone %s responded more than once' % drone_id
			return
		self.drones_responded.append(drone_id)
		string = data['rf_data']
		# print string
		# msg = Message(string)
		# print msg
		check = [i in self.drones_responded for i in self.active_drone_ids]
		if False not in check:
			self.complete = True


def heartbeat_routine(swarm):
	print 'Sending heartbeat'
	routine = HeartbeatRoutine(swarm.active_drone_ids)
	link = communication.Link(callback=routine.recieve_response, read_timeout=2, write_timeout=2)
	messages = [communication.Message(to_id=i, from_id=1, type_id=1, payload='HEART') for i in swarm.active_drone_ids]
	for msg in messages:
		link.send_message(msg)
	time.sleep(1)
	if routine.complete:
		print 'Loop complete'
		link.close()
		return
	time.sleep(1)
	link.close()