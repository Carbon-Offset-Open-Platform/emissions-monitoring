import subprocess 

# Retrieve current power consumption from the local host
# This version retrieves the datum from the local host machine
# In other words, this program is trying to retrieve a power consumption datum
# from the machine in which it is running.
def Get_power_consumption (): 

    try: 
        # Run the ipmitool command to get power consumption in watts 
        result = subprocess.run ( 
            ['ipmitool', 'sdr', 'type', 'Current'], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True) 

        if result.returncode != 0: 
            print (f"Error executing ipmitool: {result.stderr}") 
            return None 

        # Parse the output to find the power consumption (in Watts or Amps) 
        for line in result.stdout.splitlines (): 
            if "Watts" in line or "W" in line: 
                # Extract and return the numeric value 
                # for power consumption 
                parts = line.split () 
                
                for part in parts: 
                    if part.replace('.', '', 1).isdigit (): 
                        return float (part) 

        print ("Power consumption data not found.") 
        return None 

    except Exception as e: 
        print (f"Exception occurred: {e}") 
        return None
    
# End - Get_power_consumption ()
