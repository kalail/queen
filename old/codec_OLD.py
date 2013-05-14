import re


class Packet(object):
	"""Packet

	A single packet.

	"""

	def __init__(self, to_id, from_id, msg_type_id, msg_string):
		"""Create a packet from the given data."""

		self.to_id = to_id
		self.from_id = from_id
		self.msg_type_id = msg_type_id
		self.msg_string = msg_string

		def __repr__(self):
			return 'Packet type %s from %s to %s' % (self.msg_type, self.from_id, self.to_id)


class Codec(object):
	"""Codec

	Decodes packets into expected values.

	"""
	def __init__(self, structure):
		self.structure = structure
		self.__create_pattern__()

		
	def __create_pattern__(self):
		"""Return regex pattern based on given structure dictionary."""

		# Translate packet structure
		regex_args = []
		regex_args.append(self.structure['TO_LENGTH'])
		regex_args.append(self.structure['FROM_LENGTH'])
		regex_args.append(self.structure['MSG_TYPE_LENGTH'])
		regex_args.append(self.structure['TERMINATOR'])
		# Create packet matching regular expression
		self.pattern = re.compile(r'^(?P<to>\d{%s})(?P<from>\d{%s})(?P<msg_type>\d{%s})(?P<msg_string>.*)(?P<terminator>%s)$' % tuple(regex_args))


	def decode(self, packet_string):
		# Match pattern against string
		matched_pattern = self.pattern.match(packet_string)
		
		# Check for corrupt packet.
		if not matched_pattern:
			raise IOError('Packet is corrupt')

		# Extract and cast data
		to_id = int(matched_pattern.group('to'))
		from_id = int(matched_pattern.group('from'))
		msg_type_id = int(matched_pattern.group('msg_type'))
		msg_string = matched_pattern.group('msg_string')
		# Create packet
		packet = Packet(to_id, from_id, msg_type_id, msg_string)
		return packet


	def encode(self, packet):
		packet_string = '{0:0{1:d}d}{2:0{3:d}d}{3:0{4:d}d}{5}{6}'.format(
			packet.to_id,
			self.structure['TO_LENGTH'],
			packet.from_id,
			self.structure['FROM_LENGTH'],
			packet.msg_type_id,
			self.structure['MSG_TYPE_LENGTH'],
			packet.msg_string,
			self.structure['TERMINATOR'],
		)
		return packet_string