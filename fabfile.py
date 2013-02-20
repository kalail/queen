from fabric.api import *


env.hosts = [
	'108.84.166.27'
]
env.user = 'pi'


def prepare_raspberry_pi():
	pass

def pull():
	with cd('virtualenvs/queen/queen'):
		run('git pull')

def deploy():
	pass
