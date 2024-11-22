# SCOOP Server Emissions Monitor
# Workload Manager

# Initialize the workload process ID for the first round
workload_pid = 0

# This code runs in an infinite loop
while True:
    time_of_day = Get_time_of_day ()
    
    # Get the desired loading for this time-of-day
    loading_target = Get_load_target (time_of_day)

    # If this is not the first time around, stop the currently
    # running workload
    if workload_pid != 0: Kill_process (workload_pid)
    
    # Launch new instance of PTU.
    # if PTU is not available, use Prime95
    Launch_PTU (loading_target)
    
    # Go to sleep for the next 15 minutes.
    Sleep (15, 'minutes')