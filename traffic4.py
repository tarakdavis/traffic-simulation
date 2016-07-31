import numpy as np
# import matplotlib.pyplot as plt
import random
import statistics as st


class Car:
    def __init__(self, position):
        self.max_speed = 33.33333
        self.size = 5
        self.speed = 0
        self.accel = 2
        self.slow_percentage = 0.1
        self.position = np.array([position, position + self.size])

    def __repr__(self):
        return "position: {}, speed: {}".format(self.position, self.speed)

# Car accelerates normally.
    def accelerate_car(self):
        self.speed += self.accel

# Car decelerates normally.
    def decelerate_car(self):
        self.speed -= self.accel

# Get distance between cars.
    def is_car_close(self, other):
        distance = other.position[1] - self.position[0]
        if distance <= self.speed:
            if self.speed >= other.speed:
                return True

# Car matches speed.
    def match_speed(self, other):
        self.speed == other.speed

# Car randomly slows 2 m/s at 10% chance
    def is_random_slowdown(self):
        if random.random() <= self.slow_percentage:
            return True


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
            if position > self.length:
                position = position % self.length


class Simulation:
    def __init__(self, road):
        self.time = 60
        self.speeds = []
        self.road = road

    def get_mean(self):
        return st.mean(self.speeds)

    def get_stdev(self):
        return st.stdev(self.speeds)

    def run(self):
        for seconds in range(self.time):
            for index, car in enumerate(road.cars):
                car.accelerate_car()
                if car.speed >= car.max_speed:
                    car.decelerate_car()
                elif car.speed < 0:
                    car.speed = 0
                elif car.is_random_slowdown():
                    car.decelerate_car()
                elif car.is_car_close(road.cars[index]):
                    car.match_speed(road.cars[index])
                self.speeds.append(car.speed)
        mean = self.get_mean()
        stdev = self.get_stdev()
        speed_limit = int(round(mean + stdev))
        print("Average Speed: {}, Standard Deviation: {}, Speed Limit: {}".format(mean, stdev, speed_limit))


road = Road()
road.populate_cars()
simulation = Simulation(road)
simulation.run()
