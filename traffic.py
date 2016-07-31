import numpy as np
# import matplotlib.pyplot as plt
import statistics
import random


class Car:
    def __init__(self, position):
        self.max_speed = 120
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

    def reset_track(self, road):
        if self.position > road.length:
            self.position = self.position % road.length


class Road:
    def __init__(self, length=1000, cars=30):
        self.length = length
        self.cars = cars
        self.list_of_cars = []

# Place cars on road.
    def populate_cars(self, car):
        position = 0
        for _ in range(self.cars):
            self.list_of_cars.append(Car(position))
            position += (self.length / self.cars)
            return self.list_of_cars


class Simulation:
    def __init__(self, time=60, speeds=[]):
        self.time = time
        self.speeds = speeds

    # def get_mean(self):
    #     return np.mean(self.speeds)
    #
    # def get_stdev(self):
    #     return np.std(self.speeds)

    def run_simulation(self, car, road):
        road = Road()
        road.populate_cars(car)
        for second in range(self.time):
            for idx, item in road.list_of_cars:
                car.change_speed()
                car.accelerate_car()
                car.random_slowdown()
                car.decelerate_car()
                self.speeds.append(car.speed)
        # mean = self.get_mean()
        # stdev = self.get_stdev()
        # speed_limit = int(round(mean + stdev))
        return self.speeds
        # mean, stdev, speed_limit


def main():
    car = Car(
    simulation = Simulation(car)
    simulation.run_simulation(Car, Road)


if __name__ == '__main__':
    main()
