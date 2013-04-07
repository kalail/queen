import serial
import communication

# def get_active_drones():
# 	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
# 	send_msg = '0;1;0;heartbeat\n'
# 	port.write(send_msg)
# 	drones = []
# 	msg = port.readline()
# 	if not msg:
# 		return None
# 	drone_id = msg[2]
# 	drones.append(drone_id)
# 	return drones

def get_active_drones(link):
	messages = []
	# Send heartbeat
	heartbeat = communication.Message(to_id=0, from_id=1, type_id=0, payload='HEARTBEAT')
	link.send_message(heartbeat)
	# Read mesages until timeout
	while True:
		message = link.read_message()
		# Check for timeout
		if not message:
			break
		# Add to messages
		messages.append(message)
	# Create list of drones
	drones = [msg.from_id for msg in messages]
	return drones