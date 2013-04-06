import serial

def get_active_drones():
	port = serial.Serial('/dev/ttyUSB0', 9600)
	port.write('0;1;0;GabeIsADick!\n')
	drones = []
	
	msg = port.readline()
	drone_id = msg[2]
	drones.append(drone_id)

	return drones