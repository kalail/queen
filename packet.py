import re

rec_packet = '1234packet_data\n'

# Create packet matching regular expression
pattern = re.compile(r'^(?P<to>[0-9]{1})(?P<from>[0-9]{1})(?P<cmd>[0-9]{2})(?P<packet>.*)(?P<terminator>\n)$')
# Match packet
matched = pattern.match(rec_packet)
# Check if packet was matched successfully
if matched:
	# Get parsed dictionary
	parsed = matched.groupdict()
	print parsed