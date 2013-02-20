"""Communication

Handles all communication between the queen and drones using high level
interfaces.

"""

import queen.settings as settings
import serial


from .parser import Parser
from .codec import Codec, Packet
from .link import Link


class Communication(object):
	"""Communication

	Implements the queens communication functionality.
	
	"""

	def __init__(self):
		"""Initialize

		Initialize all helpers and establish serial connection.

		"""
		self.active = False
		# Open port
		config = settings.SERIAL
		self.serial = serial.Serial(config['DEVICE'], config['BAUD'], timeout=config['TIMEOUT'], writeTimeout=config['WRITE_TIMEOUT'])
		# Create helpers
		self.links = []
		self.codec = Codec(settings.PACKET_STRUCTURE)
		self.parsers = self.__create_parsers__()


	def __create_parsers__(self):
		parsers = []
		for idx, msg in enumerate(settings.MESSAGES):
			parser = Parser(idx, msg['name'], msg['parameters'])
			parsers.append(parser)
		return parsers


	def create_link(self, drone_id):
		"""Create Link

		Creates and returns a link to specified drone.

		"""
		# Check if link already exists
		for link in self.links:
			if link.id == drone_id:
				raise RuntimeError('link already exists')

		# Create message
		p = self.get_parser('CreateLink')
		msg = p.compose({
			'startup_delay': 10,
		})
		# Create packet
		packet = Packet(drone_id, settings.QUEEN_ID, p.msg_id, msg)
		self.codec.encode(packet)
		
		# Create new link
		new_link = Link(drone_id)
		self.links.append(new_link)
		return new_link

	def get_parser(self, name):
		for parser in self.parsers:
			if parser.name == name:
				return parser

	def destroy_link(self, drone_id):
		"""Destroy Link

		Close and destroy the link to the specifies drone.

		"""
		# Find and get link
		remove_link = None
		for link in self.links:
			if link.id == drone_id:
				remove_link = link
				break
		# Remove link from list
		self.links.remove(remove_link)
		# Destroy link
		remove_link.teardown()