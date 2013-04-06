
import helpers
import time

if __name__ == '__main__':
	time.sleep(2)
	while True:
		active_drones = helpers.get_active_drones()
		print active_drones
		time.sleep(1)
