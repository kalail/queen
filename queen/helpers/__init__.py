import communication
import serial
from .process import initialize_worker


def simple_ping():
	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
	send_msg = '0\n'
	port.write(send_msg)
	messages = []
	while True:
		msg = port.readline()
		if not msg:
			break
		messages.append(msg)
	return messages

def simple_heartbeat():
	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
	send_msg = '0;1;0;HEARTBEAT\n'
	port.write(send_msg)
	messages = []
	while True:
		msg = port.readline()
		if not msg:
			break
		messages.append(msg)
	return messages


def get_active_drones(link):
	messages = []
	# Send heartbeat
	heartbeat = communication.Message(to_id=0, from_id=1, type_id=0, payload='TheFirstSwarm')
	link.send_message(heartbeat)
	# Read mesages until timeout
	while True:
		message = link.read_message()
		# Check for timeout
		if not message:
			break
		# Add to messages
		messages.append(message)
		print 'Drone ID %s active' % message.from_id
	# Create list of drones
	drones = [msg.from_id for msg in messages]
	return drones

