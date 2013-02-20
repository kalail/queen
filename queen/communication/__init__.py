"""Communication

Handles all communication between the queen and drones using high level
interfaces.

"""

import queen.settings as settings
import serial
import core

from .parser import Parser
from .codec import Codec



class Communication(object):
	"""Communication

	Implements the queens communication functionality.
	
	"""

	def __init__(self, device=settings.SERIAL_DEVICE, baud=settings.SERIAL_BAUD):
		"""Initialize

		Initialize all helpers and establish serial connection.

		"""
		# Assign class variables
		self.device = device
		self.baud = baud
		self.links = []
		self.active = False
		# Open port
		self.open()
		# Create helpers
		self.codec = Codec(settings.PACKET_STRUCTURE)
		self.__create_parsers__()


	def __create_parsers__(self):
		self.parsers = []
		for idx, msg in enumerate(settings.MESSAGES):
			parser = Parser(idx, msg['name'], msg['parameters'])
			self.parsers.append(parser)


	def open(self, device=None, baud=None):
		"""Open

		Create a serial port and update class variables.
		
		"""
		# Check if port is already open
		if self.active:
			self.close()

		# Update class variables if given
		if device and baud:
			self.device = device
			self.baud = baud

		# Attempt to open serial port
		try:
			self.port = serial.Serial(self.device, self.baud)
			self.active = True
			print 'port activated'
		except serial.serialutil.SerialException:
			self.port = None
			self.active = False
			print 'error during port activation'


	def reset(self):
		"""Reset

		Close and recreate the open serial port.

		"""
		self.close()
		self.open()


	def close(self):
		"""Close

		Close the active connection to the serial port.

		"""
		self.port.close()
		self.active = False


	def create_link(self, drone_id):
		"""Create Link

		Creates and returns a link to specified drone.

		"""
		# Check if link already exists
		for link in self.links:
			if link.id == drone_id:
				print 'Link already exists'
				return
		# Create new link
		new_link = core.link.Link(drone_id)
		self.links.append(new_link)
		return new_link


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