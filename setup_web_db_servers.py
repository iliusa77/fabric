from fabric.api import *
from fabric import *
from fabtools import *
from common import dist_upgrade

env.hosts = [
    'vagrant@192.168.33.15',
    'vagrant@192.168.0.106'
    ]
# env.parallel = 'True'
env.warn_only='True'

env.roledefs = {
    'web': ['vagrant@192.168.33.15'],
    'db': ['vagrant@192.168.0.106']
}



# @task (default=True)
# @roles('web','db')
# def dist_upgrade():
#     sudo('apt update && apt upgrade -y')

@task
@roles('web')
def install_nginx():
    sudo('apt install nginx -y')

@task 
def remove_nginx():
    sudo('service mysql stop && apt remove --purge nginx -y')

@task
@roles('db')
def install_mysql():
    sudo('apt install mysql-server mysql-client -y')

@task 
def remove_mysql():
    sudo('service mysql stop && apt remove --purge mysql-server mysql-client -y')

@task
def setup():
    dist_upgrade()