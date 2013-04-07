"""Queen

Creates the majestic queen bot.

	"All your drones are belong to her".

	Arguments
		None

"""
# import helpers
import time
import communication as comms

if __name__ == '__main__':
	# Sleep for 2 seconds
	# TODO: Make CLI argument
	time.sleep(2)
	# Setup link
	link = comms.Link()
	send_msg = comms.Message(to_id=0, from_id=1, type_id=0, payload='HEATRTBEAT')
	send_msg_lost = comms.Message(to_id=7, from_id=1, type_id=8, payload='HEATRTBEAT')
	while True:
		link.send_message(send_msg)
		link.send_message(send_msg_lost)
		rec_msg = link.read_message()
		print rec_msg.from_id
		link.send_message(send_msg_lost)
		# time.sleep(1)
	# Send heartbeat
	# Serially read responding drones
	# Record time
	# Setup Process pool
	# Start heartbeat loop