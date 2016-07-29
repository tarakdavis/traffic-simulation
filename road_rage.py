import numpy as np
import matplotlib.pyplot as plt
import statistics


class Car:
    def __init__(self, position, car_in_front=None):
        self.max_speed = 33.33
        self.size = 5
        self.speed = 0
        self.accel = 2
        self.slow_percentage = 0.1
        self.position = np.array([position, position + self.size])

# Car accelerates normally.
    def __init__(self, max_speed=33.33, size=5, accel=2, location=0, slow_percentage=0.1, position):
        self.max_speed = max_speed
        self.size = size
        self.accel = accel
        self.location = location
        self.slow_percentage = slow_percentage
        self.position = np.array([position, position + 5])

    #Car accelerates normally.
    def accelerate_car(self):
        self.speed += self.accel

# Car matches speed of car in front if about to hit.
    def is_car_in_front(self, car_in_front):
        distance = car_in_front.position[0] - self.position[1]
        if distance <= self.speed:
            if self.speed >= car_in_front.speed:
                self.speed == car_in_front.speed

# Car randomly slows 2 m/s at 10% chance
    def is_car_slowing(self):
        if random.random() == self.slow_percentage:
            self.speed -= self.accel

    """Car matches speed of car in front if about to hit."""
    def is_car_close(self):
        pass

    # Car randomly slows 2 m/s at 10% chance
    def is_car_slowing(self):
        if random.random() == self.slow_percentage:
            self.accel -= 2
            return self.accel


class Road:
    def __init__(length=1000, cars=30, list_of_cars=[]):
        self.length = length
        self.cars = cars
        self.list_of_cars = []

    """Place cars on road"""
    def populate_cars(self):
        position = 0
        for _ in range(self.cars):
            self.list_of_cars.append(Car(position))
            position += (self.length / self.cars)
        return self.list_of_cars

class Simulation:
    def __init__(self, max_time=60):
        self.max_time = max_time

    def run_simulation():
        pass
