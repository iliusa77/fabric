from fabric.api import *
from fabric import *
from fabtools import *

# env.hosts = ['']
# env.parallel = 'True'
# env.warn_only='True'

@task
def get_hostname():
    run('hostname')

@task
def status():
    run('uptime')
    run('cat /proc/loadavg')
    run('free')
    run('df -h')

@task
def dist_upgrade():
    sudo('apt update && apt upgrade -y')
