# -*- coding: utf-8 -*-
def get_requested_watts(data):
    """
    Extracts the RequestedWatts from the power data JSON.

    Parameters:
    power_data (dict): The JSON data of the power subsystem.

    Returns:
    int: The requested watts.
    """
    return data.get("Allocation", {}).get("RequestedWatts", None)

def get_average_consumed_watts(data):
    """
    Extracts the AverageConsumedWatts from the power data JSON.

    Parameters:
    data (dict): The JSON data of the power subsystem.

    Returns:
    int: The average consumed watts, or None if not found.
    """
    return data.get("PowerControl", [{}])[0].get("PowerMetrics", {}).get("AverageConsumedWatts", None)


