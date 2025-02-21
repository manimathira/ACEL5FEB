import yaml
import pyeapi
file = open ('vlans.yml' , 'r')
vlan_dict = yaml.safe_load(file)
print (vlan_dict)
for switch in vlan_dict['switches']:
  connect = pyeapi.connect_to(switch)
  vlan_api = connect.api('vlans')
  for vlan in vlan_dict['vlans']:
    vlan_id = vlan['id']
    vlan_name = vlan['name']
    vlan_api.create(vlan_id)
    vlan_api.set_name(vlan_id, vlan_name)

for switch in vlan_dict ['switches']:
    configured_vlans = vlan_api.getall()
    print (configured_vlans)
    interface_api = connect.api("ipinterfaces")
    for configured_vlan in configured_vlans:
        # print (configured_vlan)
        commands = ["interface vlan {}".format(configured_vlan), "ip address 192.168.{}.254/24".format(configured_vlan), "no autostate", "no shutdown"]
        config = connect.config(commands)
        intname = ("Vlan{}".format(configured_vlan))
        getintvlans = interface_api.get(intname)
        print (getintvlans)