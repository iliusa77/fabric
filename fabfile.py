from fabric.api import *
from fabric import *
from fabtools import *
from common import dist_upgrade
from fabric.contrib.files import *

env.hosts = [
    'vagrant@192.168.5.161'
    ]
# env.parallel = 'True'
env.warn_only='True'

env.roledefs = {
    'web': ['vagrant@192.168.5.161'],
    'db': ['vagrant@192.168.5.161']
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
@roles('db')
def configure_mysql():
    mysql_config_variables = {
            'bind-address': '1.2.3.4'
        }
    upload_template(
        filename='templates/mysql/mysql_config',
        destination='/etc/mysql/mysql.conf.d/mysqld.cnf',
        context=mysql_config_variables,
        use_sudo=True
        )
    sudo('systemctl unmask mysql.service && service mysql restart')
    
@task 
def remove_mysql():
    sudo('service mysql stop && apt remove --purge mysql-server mysql-client -y')

@task
def autoremove():
    sudo('apt-get autoremove -y')

@task
def setup():
    dist_upgrade()
    install_nginx()
    install_mysql()
    configure_mysql()

@task
def clear():
    remove_nginx()
    remove_mysql()
    autoremove()