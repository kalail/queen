from fabric.api import *


env.hosts = [
	'192.168.1.144'
]
env.user = 'pi'


def prepare_raspberry_pi():
	pass

def remote_pull():
	with cd('virtualenvs/queen/queen'):
		run('git pull')

def deploy():
	local('git commit -a')
	local('git push origin')
	remote_pull()
