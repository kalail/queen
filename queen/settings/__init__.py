import os

from queen.communication.messages import messages

# Load correct settings
try:
	# Get environment variable
	env = os.environ["DC_ENVIRONMENT"]
	if env == "production":
		# Import production settings
		from .production import *
except KeyError, e:
	# import development settings
	from .development import *


# Startup delay in seconds
STARTUP_DELAY = 3

# List of available drones
DRONES = [
	'test',
]

SERIAL = {
	'DEVICE': 'dev/tty0',
	'BAUD': 9600,
	'TIMEOUT': 2.0,
	'WRITE_TIMEOUT': 2.0,
}

PACKET_STRUCTURE = {
	'TO_LENGTH': 1,
	'FROM_LENGTH': 1,
	'MSG_TYPE_LENGTH': 2,
	'MSG_DELIMETER': ';',
	'TERMINATOR': '\n',
}

MESSAGES = messages

RASPBERRY_PI = {
	'ip': '108.84.166.27',
}

QUEEN_ID = 1