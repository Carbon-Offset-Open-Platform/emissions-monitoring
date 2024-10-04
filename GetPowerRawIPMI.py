
# BMC connection details
bmc_ip = '192.168.1.25'
username = 'admin'      # Replace with actual BMC username
password = 'password'   # Replace with actual BMC password

# Retrieve power reading from server at BMC address 192.168.1.25
# Install the pyghmi library before running, using the bash command
#
# pip install pyghmi
#
def Get_power_consumption (bmc_ip, username, password):

    # Command to get SDR (sensor data records)
    command = f"ipmitool -I lanplus -H {bmc_ip} -U {username} -P {password} sdr"

    # Initialize IPMI session with the BMC
    ipmi_session = command.Command (bmc_ip, bmc_user, bmc_password)

    # Fetch the SDR (Sensor Data Records)
    sdr_records = ipmi_session.get_sdr ()

    # Function to extract power consumption from SDR records
    def get_power_consumption (sdr):
        for record in sdr:
            # Look for sensors related to power consumption
            if 'Power' in record['name']:  
                sensor_reading = record.get ('reading', None)
                sensor_unit = record.get ('units', None)
                
                if sensor_reading is not None and sensor_unit:
                    print (f"Power Consumption: {sensor_reading} {sensor_unit}")
                    return sensor_reading, sensor_unit
                
        print ("Power consumption data not found.")
        return None

    # Parse the SDR records for power consumption
    power_data = get_power_consumption (sdr_records)

    # Close the IPMI session 
    # (optional, as pyghmi handles sessions dynamically)
    ipmi_session.ipmi_session.logout ()
    
# End Get_power_consumption ()
