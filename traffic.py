import numpy as np
# import matplotlib.pyplot as plt
# import statistics
import random


class Car:
    def __init__(self, position):
        self.max_speed = 120
        self.size = 5
        self.speed = 0
        self.accel = 2
        self.slow_percentage = 0.1
        self.position = np.array([position, position + self.size])
        #self.position =[]

    def __repr__(self):
        return "position: {}, speed: {}".format(self.position, self.speed)

# Car accelerates normally.
    def accelerate_car(self):
        self.speed += self.accel

    def decelerate_car(self):
        self.speed -= self.accel
        if self.speed < 0:
            self.speed = 0
        elif self.speed >= self.max_speed:
            self.decelerate_car()
        else:
            self.accelerate_car()

# Car matches speed of car in front if about to hit.
    def change_speed(self, other):
        distance = other.position[0] - self.position[1]
        if distance <= self.speed:
            if self.speed >= other.speed:
                self.speed == other.speed
        else:
            self.accelerate_car()

# Car randomly slows 2 m/s at 10% chance
    def random_slowdown(self):
        if random.random() == self.slow_percentage:
            self.decelerate_car()
        else:
            self.accelerate_car()

    def reset_track(self):
        if self.position > Road.length:
            self.position = self.position % Road.length


class Road:
    def __init__(self, length=1000):
        self.length = length
        self.cars = []

# Place cars on road.

    def populate_cars(self, amount =30):
        position = 0
        for _ in range(amount):
            self.cars.append(Car(position))
            position += (self.length / amount)


class Simulation:
    def __init__(self, road):
        self.time = 60
        self.speeds = []
        self.road = road

    def run(self):
        for seconds in range(self.time):
            for car in self.road.cars:
            # for index, items in enumerate range(road):
                car.change_speed(other)
                car.random_slowdown()
                car.decelerate_car()
                self.speeds.append(car.speed)
                print(car.position)
                print(car.speed)

road = Road()
road.populate_cars()
#print(road.list_of_cars)
simulation = Simulation(road)
simulation.run()
