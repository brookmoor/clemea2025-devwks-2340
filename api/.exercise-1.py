import ctb

manager_ip = "<your-manager-ip>"
username = "<username>"
password = "<password>"

response = ctb.login(manager_ip, username, password)
print (response)

nodes = ctb.get_nodes()
print(nodes.json())

print (nodes.json()[0]["id"])

inputs = ctb.get_input_types()
print(inputs.json())

new_inputs = ctb.create_input("api_input", "udp_listener", "2", "4789", False)
print (new_inputs.status_code)
print(new_inputs.json())

new_dests = ctb.create_destination("api_dest", "udp", "10.0.54.250", "4789", False)
print (new_dests.status_code)
print (new_dests.json())

new_subs = ctb.create_subscription("7", "5")
print (new_subs.status_code)
print (new_subs.json())

current_input = ctb.get_inputs("7")
print(current_input.json())

dests = ctb.get_destinations("5")
print(dests.json())