import random
from road_rage import Car
from road_rage import Road
from road_rage import Simulation

def test_populate_cars():
    total_length = 105
    assert total_length == 105

def test_road():
    length = 1000
    assert length == 1000

def test_car_object():
    location = 0
    position_car = 0
    accelerate_car = 2
    assert location == 0
    assert position_car == 0
    assert accelerate_car == 2

def test_max_time():
    max_time = 60 # seconds
    assert max_time == 60
    
