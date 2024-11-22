# -*- coding: utf-8 -*-
def get_requested_watts(power_data):
    """
    Extracts the RequestedWatts from the power data JSON.

    Parameters:
    power_data (dict): The JSON data of the power subsystem.

    Returns:
    int: The requested watts.
    """
    return power_data.get("Allocation", {}).get("RequestedWatts", None)
