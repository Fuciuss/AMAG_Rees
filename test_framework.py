import pytest
from framework import VehicleData

@pytest.fixture
def vehicle_data_obj():
    obj = VehicleData('./data.npy')
    return obj

def test_runs(vehicle_data_obj):
    assert vehicle_data_obj is not None

def test_by_id(vehicle_data_obj):
    segment = vehicle_data_obj.by_id(1)
    assert len(segment) > 1
    
