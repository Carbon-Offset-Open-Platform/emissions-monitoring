server_ID = 0	# Not used for a single-machine environment.

interval = 1 	# Power consumption sampling interval set to 1 second.

while True:
    timestamp = Get_time_of_day ()
    # Retrieve server power consumption datum
    current_power = Get_power_consumption (server_ID)
    Write_power (server_ID, timestamp, current_power)

    # Go back to sleep until the time for the next readout
    Sleep (1, 'seconds')