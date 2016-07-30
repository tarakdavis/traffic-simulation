import numpy as np
# import matplotlib.pyplot as plt
# import statistics
import random


class Car:
    def __init__(self, position):
        self.max_speed = 33.33
        self.size = 5
        self.speed = 0
        self.accel = 2
        self.slow_percentage = 0.1
        self.position = np.array([position, position + self.size])
        self.car_in_front = None

    def __repr__(self):
        return "position: {}, speed: {}".format(self.position, self.speed)

# Car accelerates normally.
    def accelerate_car(self):
        self.speed += self.accel

    def decelerate_car(self):
        self.speed -= self.accel
        if self.speed < 0:
            self.speed = 0

    def is_car_speeding(self):
        if self.speed >= self.max_speed:
            self.speed <= self.max_speed

# Car matches speed of car in front if about to hit.
    def is_car_in_front(self, car_in_front):
        distance = car_in_front.position[0] - self.position[1]
        if distance <= self.speed:
            if self.speed >= car_in_front.speed:
                self.speed == car_in_front.speed

# Car randomly slows 2 m/s at 10% chance
    def is_car_slowing(self):
        if random.random() == self.slow_percentage:
            self.decelerate_car()
        else:
            self.accelerate_car()

    def is_track_ending(self):
        self.position = (self.position + self.speed) % Road.length


class Road:
    def __init__(self, length=1000, cars=30):
        self.length = length
        self.cars = cars
        self.list_of_cars = []

# Place cars on road.
    def populate_cars(self):
        position = 0
        for _ in range(self.cars):
            self.list_of_cars.append(Car(position))
            position += (self.length / self.cars)

    def relative_car(self):

# class Simulation:
#     pass

road = Road()
road.populate_cars()
print(road.list_of_cars)
#
# def main():
#     time = 60
#     speeds = []
#     starting_positions = Road.populate_cars()
#     for seconds in time:
#
#
# if __name__ == '__main__':
#     main()
