import serial
import communication

def get_active_drones():
	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
	send_msg = '0;1;0;heartbeat\n'
	port.write(send_msg)
	drones = []
	msg = port.readline()
	if not msg:
		return None
	drone_id = msg[2]
	drones.append(drone_id)
	return drones

def get_active_drones_new():
	link = communication.Link()
	send_msg = communication.Message(to_id=0, from_id=1, type_id=0, payload='HEATRTBEAT')
	link.send_message(send_msg)
	drones = []
	rec_msg = link.read_message()
	if not rec_msg:
		return None
	drones.append(rec_msg.from_id)
	return drones