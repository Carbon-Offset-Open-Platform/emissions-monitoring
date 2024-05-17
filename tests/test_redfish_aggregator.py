from .context import redfish_aggregator
import pytest

def test_get_requested_watts():
    # Sample JSON data
    sample_data = {
        "@odata.id": "/redfish/v1/Chassis/1U/PowerSubsystem",
        "@odata.type": "#PowerSubsystem.v1_1_1.PowerSubsystem",
        "Allocation": {
            "AllocatedWatts": 1200,
            "RequestedWatts": 1500
        },
        "Batteries": {
            "@odata.id": "/redfish/v1/Chassis/1U/PowerSubsystem/Batteries"
        },
        "CapacityWatts": 2000,
        "Id": "PowerSubsystem",
        "Name": "Power Subsystem for Chassis",
        "PowerSupplies": {
            "@odata.id": "/redfish/v1/Chassis/1U/PowerSubsystem/PowerSupplies"
        },
        "PowerSupplyRedundancy": [
            {
                "MaxSupportedInGroup": 2,
                "MinNeededInGroup": 1,
                "RedundancyGroup": [
                    {
                        "@odata.id": "/redfish/v1/Chassis/1U/PowerSubsystem/PowerSupplies/Bay1"
                    },
                    {
                        "@odata.id": "/redfish/v1/Chassis/1U/PowerSubsystem/PowerSupplies/Bay2"
                    }
                ],
                "RedundancyType": "Failover",
                "Status": {
                    "Health": "OK",
                    "State": "UnavailableOffline"
                }
            }
        ],
        "Status": {
            "Health": "OK",
            "State": "Enabled"
        }
    }

    # Test case
    assert get_requested_watts(sample_data) == 1500

if __name__ == "__main__":
    pytest.main()

