import ctb

manager_ip = "<your-manager-ip>"
username = "<username>"
password = "<password>"

response = ctb.login(manager_ip, username, password)
print (response)

nodes = ctb.get_nodes()
print(nodes.json())

node_id = nodes.json()[0]["id"]
print (node_id)

input_types = ctb.get_input_types()
print(input_types.json())

new_input = ctb.create_input("api_input", "udp_listener", node_id, "2055", False)
print (new_input.status_code)
print (new_input.json())
new_input_id = new_input.json()["id"]
print (new_input_id)

new_dest = ctb.create_destination("api_dest", "udp", "10.0.54.121", "20001", False)
print (new_dest.status_code)
print (new_dest.json())
new_dest_id = new_dest.json()["id"]
print (new_dest_id)

new_sub = ctb.create_subscription(new_input_id, new_dest_id)
print (new_sub.status_code)
print (new_sub.json())

current_input = ctb.get_inputs(new_input_id)
print(current_input.json())

current_dest = ctb.get_destinations(new_dest_id)
print(current_dest.json())