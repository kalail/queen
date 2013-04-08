import signal

def initialize_worker():
	"""Initialize Worker

	Sets worker processes to ignore SIGINT.

	"""
	signal.signal(signal.SIGINT, signal.SIG_IGN)
