import yaml
file = open('yaml-example.yaml', 'r')
data_model_raw = file.read()
data_model = yaml.safe_load(data_model_raw)
for leaf,interfaces in data_model.items():
    print(f"configuration on {leaf}")
    for interface,address in interfaces.items():
        print(f"interface {interface}")
        print(f"  no switchport")
        print(f"  ip address {address}")