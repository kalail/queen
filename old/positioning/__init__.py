
class Position(object):
	"""Represents a postion and orientation in the arena."""

	def __init__(self, x, y, r=0):
		self.x = x
		self.y = y
		self.r = r % 360

	def same_area(self, position, tolerance=1.0):
		"""Returns whether the position is aproximately equal to the given position within said tolerance."""

		t = tolerance
		if self.x - t <= position.x <= self.x + t:
			if self.y - t <= position.y <= self.y + t:
				return True
		# Else
		return False

	def same_facing(self, position, tolerance=15.0):
		"""Returns whether the position is aproximately equal to the given position within said tolerance."""

		t = tolerance
		diff = abs(position.r - self.r)

		if diff >= 180:
			diff = 360 - diff

		if diff <= t:
			return True
		# Else
		return False