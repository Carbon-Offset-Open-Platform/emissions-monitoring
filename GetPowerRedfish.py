import requests
import json

# Get a power reading from machine at URL BMC_ip using a Redfish REST call
def Get_power_consumption (BMC_ip, username, password):
    try:
        # Redfish Power endpoint for retrieving power consumption
        power_url = f"https://{BMC_ip}/redfish/v1/Chassis/1/Power"

        # Create a session and authenticate
        session = requests.Session()
        session.auth = (username, password)
        # In case the server uses self-signed certificates
        session.verify = False  

        # Make a GET request to retrieve power data
        response = session.get(power_url)

        if response.status_code != 200:
            print(f"Error: Unable to retrieve power data. HTTP Status Code: {response.status_code}")
            return None

        # Parse the JSON response
        power_data = response.json()

        # Extract the power consumption from the "PowerControl" section
	  # (usually in Watts)
        power_control = power_data.get ('PowerControl', [])
        if power_control:
            for power_item in power_control:
                if 'PowerConsumedWatts' in power_item:
                    return power_item['PowerConsumedWatts']

        print ("Power consumption data not found in Redfish response.")
        return None

    except requests.exceptions.RequestException as e:
        print (f"Error connecting to Redfish API: {e}")
        return None
    
# End - Get_power_consumption ()

if __name__ == "__main__":
    # Redfish BMC details
    BMC_ip = "192.168.6.25"
    username = "admin"  # Replace with your Redfish username
    password = "password"  # Replace with your Redfish password

    power_consumption = Get_power_consumption (BMC_ip, username, password)
    if power_consumption is not None:
        print (f"Current power consumption: {power_consumption} Watts")
    else:
        print ("Could not retrieve power consumption.")