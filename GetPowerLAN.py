# Code fragment to retrieve the power consumption from a machine in the LAN
# The Baseboard Management Controller (BMC) management port, management account
# name and password are stored in bmc_ip, username and password, respectively.
         
import subprocess


# IPMI credentials and BMC address
bmc_ip = "192.168.1.25"
username = "admin"      # Replace with actual username
password = "password"   # Replace with actual password

def Get_power_consumption (bmc_ip, username, password):

    # Command to get SDR (sensor data records)
    command = f"ipmitool -I lanplus -H {bmc_ip} -U {username} -P {password} sdr"

    # Execute the command
    try:
        result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            output = result.stdout
            # Extract power consumption reading
            for line in output.splitlines():
                if "Power Consumption" in line:
                    print(line)
        else:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# End - Get_power_consumption ()