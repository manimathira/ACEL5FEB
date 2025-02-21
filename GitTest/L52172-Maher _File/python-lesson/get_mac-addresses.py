import yaml
import pyeapi
file = open('leafs.yaml', 'r')
leafs_raw = file.read()
leafs  = yaml.safe_load(leafs_raw)
mac_address_set = set()
for leaf in leafs['leafs']:
    connect = pyeapi.connect_to(leaf)
    cmds = connect.enable(["show mac address-table", "show ip interface brief"])
    mac_addresses = cmds[0]['result']['unicastTable']['tableEntries'][0]['macAddress']
    mac_address_set.add(mac_addresses)


print(mac_address_set)