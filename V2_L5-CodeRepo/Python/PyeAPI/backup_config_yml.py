import yaml
import os
import pyeapi

pyeapi.load_config('eapi.conf')

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

file = open('switches.yaml', 'r' )
switches_raw = file.read()
switches = yaml.safe_load(switches_raw)
for switch in switches:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")
