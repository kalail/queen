from fabric.api import *


env.hosts = [
	'129.105.90.207'
]
env.user = 'pi'


def prepare_raspberry_pi():
	pass

def remote_pull():
	with cd('virtualenvs/queen/queen'):
		run('git pull')

def commit():
	local('git commit -a')

def push():
	local('git push origin')
	

def deploy():
	commit()
	push()
	remote_pull()
