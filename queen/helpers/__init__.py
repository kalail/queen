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


def handle_message(data):
	drone_id = data['source_addr']
	msg = data['rf_data']
	print 'Recieved %s from drone %s' % (msg, drone_id)


def xbee_ping():
	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
	xbee = XBee(port, callback=handle_message)
	msg = '0\n'
	drone_addrs = [
		'\x00\x02',
		'\x00\x03'
	]
	while True:
		for addr in drone_addrs:
			xbee.tx(dest_addr=addr, data=msg)
		print 'Sent {0} to drones {1}'.format(msg, drone_addrs)
		time.sleep(1)

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


def dummy_callback(data):
	pass

def to_int(addr):
	if addr == '\x00\x00':
		return 0
	elif addr == '\x00\x01':
		return 1
	elif addr == '\x00\x02':
		return 2
	elif addr == '\x00\x03':
		return 3
	elif addr == '\x00\x04':
		return 4
	elif addr == '\x00\x05':
		return 5
	elif addr == '\x00\x06':
		return 6
	elif addr == '\x00\x07':
		return 7
	elif addr == '\x00\x08':
		return 8
	elif addr == '\x00\x09':
		return 9
	