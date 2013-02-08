import os

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