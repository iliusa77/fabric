### Generic Fabric library


requirements:
```
python 2.7
python-dev
fabric 1.12
```

prepare environment
```
virtualenv -p python2 .venv
. .venv/bin/activate
pip install -r requirements.txt
```

define hosts and roles in fabfile
```
vim fabfile
    env.hosts
    env.roledefs
```

run fabfile
```
fab setup
```

check server status
```
fab -f common.py --host 192.168.5.161 --user vagrant status
```