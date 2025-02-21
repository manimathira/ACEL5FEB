import yaml
import pyeapi
file = open('leafs.yaml', 'r')
leafs_raw = file.read()
leafs  = yaml.safe_load(leafs_raw)
for switches,leaf_list in leafs.items():
    for leaf in leaf_list:
        connect = pyeapi.connect_to(leaf)
        api_vlan = connect.api('vlans')
        vlans = api_vlan.getall()
        vlans_set = set()
        for vlan in vlans:
            vlans_set.add(vlan)
        print (f"the vlans on {leaf} are {vlans_set}")
        