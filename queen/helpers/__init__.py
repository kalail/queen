import serial

def get_active_drones():
	port = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
	port.write('0;1;0;GabeIsADick!\n')
	drones = []
	
	msg = port.readline()
	# Check for timeout
	if not msg:
		return None
	# Extract drone ID
	drone_id = msg[2]
	drones.append(drone_id)

	return drones