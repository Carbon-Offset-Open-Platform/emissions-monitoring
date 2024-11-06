from .context import redfishaggregator
from redfishaggregator import helpers
import pytest

Power_data = {
    "@odata.id": "/redfish/v1/Chassis/1U/Power",
    "@odata.type": "#Power.v1_7_2.Power",
    "Id": "Power",
    "Name": "Power",
    "PowerControl": [
        {
            "@odata.id": "/redfish/v1/Chassis/1U/Power#/PowerControl/0",
            "MemberId": "0",
            "Name": "System Input Power",
            "PowerAllocatedWatts": 800,
            "PowerAvailableWatts": 0,
            "PowerCapacityWatts": 800,
            "PowerConsumedWatts": 344,
            "PowerLimit": {
                "CorrectionInMs": 50,
                "LimitException": "LogEventOnly",
                "LimitInWatts": 500
            },
            "PowerMetrics": {
                "AverageConsumedWatts": 319,
                "IntervalInMin": 30,
                "MaxConsumedWatts": 489,
                "MinConsumedWatts": 271
            },
            "PowerRequestedWatts": 800,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/437XR1138R2"
                },
                {
                    "@odata.id": "/redfish/v1/Chassis/1U"
                }
            ],
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            }
        }
    ],
    "PowerSupplies": [
        {
            "@odata.id": "/redfish/v1/Chassis/1U/Power#/PowerSupplies/0",
            "FirmwareVersion": "1.00",
            "InputRanges": [
                {
                    "InputType": "AC",
                    "MaximumVoltage": 120,
                    "MinimumVoltage": 100,
                    "OutputWattage": 800
                },
                {
                    "InputType": "AC",
                    "MaximumVoltage": 240,
                    "MinimumVoltage": 200,
                    "OutputWattage": 1300
                }
            ],
            "LastPowerOutputWatts": 325,
            "LineInputVoltage": 120,
            "LineInputVoltageType": "ACWideRange",
            "Manufacturer": "ManufacturerName",
            "MemberId": "0",
            "Model": "499253-B21",
            "Name": "Power Supply Bay",
            "PartNumber": "0000001A3A",
            "PowerCapacityWatts": 800,
            "PowerSupplyType": "AC",
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Chassis/1U"
                }
            ],
            "SerialNumber": "1Z0000001",
            "SparePartNumber": "0000001A3A",
            "Status": {
                "Health": "Warning",
                "State": "Enabled"
            }
        }
    ],
    "Voltages": [
        {
            "@odata.id": "/redfish/v1/Chassis/1U/Power#/Voltages/0",
            "LowerThresholdCritical": 11,
            "LowerThresholdFatal": 10,
            "LowerThresholdNonCritical": 11.5,
            "MaxReadingRange": 20,
            "MemberId": "0",
            "MinReadingRange": 0,
            "Name": "VRM1 Voltage",
            "PhysicalContext": "VoltageRegulator",
            "ReadingVolts": 12,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/437XR1138R2"
                },
                {
                    "@odata.id": "/redfish/v1/Chassis/1U"
                }
            ],
            "SensorNumber": 11,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 13,
            "UpperThresholdFatal": 15,
            "UpperThresholdNonCritical": 12.5
        },
        {
            "@odata.id": "/redfish/v1/Chassis/1U/Power#/Voltages/1",
            "LowerThresholdCritical": 4.5,
            "LowerThresholdNonCritical": 4.75,
            "MaxReadingRange": 20,
            "MemberId": "1",
            "MinReadingRange": 0,
            "Name": "VRM2 Voltage",
            "PhysicalContext": "VoltageRegulator",
            "ReadingVolts": 5,
            "RelatedItem": [
                {
                    "@odata.id": "/redfish/v1/Systems/437XR1138R2"
                },
                {
                    "@odata.id": "/redfish/v1/Chassis/1U"
                }
            ],
            "SensorNumber": 12,
            "Status": {
                "Health": "OK",
                "State": "Enabled"
            },
            "UpperThresholdCritical": 7,
            "UpperThresholdNonCritical": 5.5
        }
    ]
}
PowerSubsystem_data = {
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

def test_get_requested_watts():
    
    # Test case
    assert helpers.get_requested_watts(PowerSubsystem_data) == 1500

def test_get_average_consumed_watts():

    # Test case
    assert helpers.get_average_consumed_watts(Power_data) == 319

if __name__ == "__main__":
    pytest.main()

