import numpy as np
# import matplotlib.pyplot as plt
import random


class Car:
    def __init__(self, position):
        self.max_speed = 120
        self.size = 5
        self.speed = 0
        self.accel = 2
        self.slow_percentage = 0.1
        self.position = np.array([position, position + self.size])
        # self.position =[]

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
        elif self.random_slowdown():
            self.decelerate_car()
        else:
            self.accelerate_car()

# Car matches speed of car in front if about to hit.
    def change_speed(self, other):
        distance = other.position[1] - self.position[0]
        if distance <= self.speed:
            if self.speed >= other.speed:
                self.speed == other.speed
        else:
            self.accelerate_car()

# Car randomly slows 2 m/s at 10% chance
    def random_slowdown(self):
        if random.random() <= self.slow_percentage:
            return True

    def reset_track(self):
        if self.position > Road.length:
            self.position = self.position % Road.length


class Road:
    def __init__(self, length=1000):
        self.length = length
        self.cars = []

# Place cars on road.

    def populate_cars(self, amount=30):
        position = 0
        for _ in range(amount):
            self.cars.append(Car(position))
            position += (self.length / amount)


class Simulation:
    def __init__(self, road):
        self.time = 60
        self.speeds = []
        self.road = road

    def get_mean(self):
        return np.mean(self.speeds)

    def get_stdev(self):
        return np.std(self.speeds)

    def run(self):
        for seconds in range(self.time):
            for index, car in enumerate(road.cars):
                # car.random_slowdown()
                car.decelerate_car()
                car.change_speed(road.cars[index])
                self.speeds.append(car.speed)
                return self.speeds

            mean = self.get_mean()
            stdev = self.get_stdev()
            speed_limit = int(round(mean + stdev))
            return mean, stdev, speed_limit
            print(self.speeds, mean, stdev, speed_limit)

road = Road()
road.populate_cars()
simulation = Simulation(road)
simulation.run()
