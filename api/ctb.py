import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ctb_manager = ""
csrftoken = ""

headers_data = {
        "Accept":"application/json, text/plain, */*",
        "Accept-Encoding":"gzip,deflate,br",
        "Accept-Language":"en-US,en;q=0.9",
        "Connection":"keep-alive",
        "Content-Type":"application/json",
        "Host": ctb_manager,
        "X-CSRFToken":"", 
        "Referer":"https://{ctb_manager}/login",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin"
        }

client = requests.session()

def login(manager_ip, username, password):
    global csrftoken
    global ctb_manager
    global headers_data

    """Login to CTB Manager - return the client session, csrf token, and session id."""

    ctb_manager = manager_ip
    login_url = f"https://{ctb_manager}/api-v1/session"
    status_url = f"https://{ctb_manager}/api-v1/install/status"

    # client = requests.session()
    client.verify = False
    r0 = client.get(status_url)

    r0 = client.get(login_url)

    login_data = { "username": username, "password": password }
    headers_data["Host"] = ctb_manager
    headers_data["Referer"] = f"https://{ctb_manager}/login"
    headers_data["X-CSRFToken"] = csrftoken

    response = client.post(login_url, data=json.dumps(login_data),  headers=headers_data, verify=False)

    # For some reason, we are issued a new csrf token after logging in, so update your local copy.
    csrftoken = response.cookies['csrftoken']

    # update headers_data with csrftoken
    headers_data["X-CSRFToken"] = csrftoken

    return response

def get_nodes():
    """Get the Broker Nodes for the CTB Manager."""
    nodes_url = f"https://{ctb_manager}/api-v1/nodes/"

    response = client.get(nodes_url, headers=headers_data, verify=False)

    return response

def get_input_types():
    """Get the different input types for the CTB Manager."""
    inputs_url = f"https://{ctb_manager}/api-v1/input-types/"

    response = client.get(inputs_url, headers=headers_data, verify=False)

    return response

def get_inputs(input_id=None):
    """Get the inputs for the CTB Manager."""
    if input_id:
        curr_inputs_url = f"https://{ctb_manager}/api-v1/inputs/{input_id}/"
    else:
        curr_inputs_url = f"https://{ctb_manager}/api-v1/inputs/"

    response = client.get(curr_inputs_url, headers=headers_data, verify=False)

    return response

def get_destinations(destination_id=None):
    """Get the different destinations for the CTB Manager."""
    if destination_id:
        dest_url = f"https://{ctb_manager}/api-v1/destinations/{destination_id}/" 
    else:  
        dest_url = f"https://{ctb_manager}/api-v1/destinations/"

    response = client.get(dest_url, headers=headers_data, verify=False)

    return response

def create_input(name, input_type, node_id, port, track_exporter_disabled):
    """Create an input for the CTB Manager."""
    create_input_url = f"https://{ctb_manager}/api-v1/inputs/"

    input_data = {
        "input_type": input_type,
        "name": name,
        "port": port,
        "node": node_id,
        "cluster": "",
        "track_exporter_disabled": track_exporter_disabled
    }

    headers_data["Referer"] = f"https://{ctb_manager}/inputs/"

    response = client.post(create_input_url, data=json.dumps(input_data), headers=headers_data, verify=False)

    return response

def delete_input(input_id):
    """Delete an input for the CTB Manager."""
    delete_input_url = f"https://{ctb_manager}/api-v1/inputs/{input_id}/"

    response = client.delete(delete_input_url, headers=headers_data,verify=False)

    return(response.status_code)

def create_destination(name, input_type, address, port, dcd_enabled):
    """Create a destination for the CTB Manager."""
    create_destination_url = f"https://{ctb_manager}/api-v1/destinations/"

    destination_data = {
        "type": input_type,
        "name": name,
        "address": address,
        "port": port,
        "dcd_enabled": dcd_enabled
    }

    headers_data["Referer"] = f"https://{ctb_manager}/destinations/"

    response = client.post(create_destination_url, data=json.dumps(destination_data), headers=headers_data, verify=False)

    return response

def delete_destination(destination_id):
    """Delete an input for the CTB Manager."""
    delete_destination_url = f"https://{ctb_manager}/api-v1/destinations/{destination_id}/"

    response = client.delete(delete_destination_url, headers=headers_data,verify=False)

    return(response.status_code)

def create_subscription(source_id, destination_id):
    """Create a subscription rule for the CTB Manager."""
    create_subscription_url = f"https://{ctb_manager}/api-v1/subscriptions/"

    subscription_data = {
        "source": source_id,
        "destination": destination_id,
        "subnets": [],
    }

    headers_data["Referer"] = f"https://{ctb_manager}/login/"

    response = client.post(create_subscription_url, data=json.dumps(subscription_data), headers=headers_data, verify=False)

    return response

def delete_subscription(subscription_id):
    """Delete an input for the CTB Manager."""
    delete_subscription_url = f"https://{ctb_manager}/api-v1/subscriptions/{subscription_id}/"

    response = client.delete(delete_subscription_url, headers=headers_data,verify=False)

    return(response.status_code)

