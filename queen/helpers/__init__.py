import communication
import serial
import time

from xbee import XBee
from .process import initialize_worker


def simple_ping():
	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
	send_msg = '0\n'
	port.write(send_msg)
	print 'Sent: %s' % send_msg
	messages = []
	while True:
		msg = port.readline()
		if not msg:
			print 'Timeout'
			break
		print 'Recieved: %s' % msg
		messages.append(msg)
	return messages

def xbee_ping():
	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
	xbee = XBee(port)
	msg = '0\n'
	drone_addrs = [
		'\x00\x02',
		'\x00\x03'
	]
	start_time = time.clock()
	for addr in drone_addrs:
		xbee.tx(dest_addr=addr, data=msg)
	print 'Sent {0} to drones {1}'.format(msg, drone_addrs)
	expected = len(drone_addrs)
	messages = []
	while expected:
		frame = xbee.wait_read_frame()
		drone_id = frame['source_addr']
		msg = frame['rf_data']
		expected -= 1
		print 'Recieved %s from drone %s' % (msg, drone_id)
		messages.append(msg)
	end_time = time.clock()
	delta = end_time - start_time
	print delta
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

