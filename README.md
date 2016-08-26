# traffic-simulation

How to run:
In order to look at the traffic sim you just need to run Road-Rage.ipynb in any web browser.  If you are interested in the python classes then you need to run traffic900.py with python3.5. Note that requirements.txt -- file contains necessary libraries to run 'traffic900.py' and 'Road-Rage.ipynb.'



Overview:
Simulation of traffic on a road and to find the optimal speed limit for the road.

We have a 1 kilometer section of road being built and do not know what the speed limit needs to be. Simulate 1 kilometer of road. Even though this road is not circular, it is treated as such in order to generate a continuous flow of traffic.

Assumptions
Drivers want to go up to 120 km/hr.
The average car is 5 meters long.
Drivers want at least a number of meters equal to their speed in meters/second between them and the next car.
Drivers will accelerate 2 m/s up to their desired speed as long as they have room to do so.
If another car is too close, drivers will match that car's speed until they have room again.
If a driver would hit another car by continuing, they stop.
Drivers will randomly (10% chance each second) slow by 2 m/s.
This section of road is one lane going one way.

Cars exiting the road start again at the beginning. This is to simulate a continuous stream of traffic. When you start the simulation, add 30 cars to the road per kilometer, evenly spaced. Then run the simulation for one minute to get a continuous, randomized stream of traffic.

The optimal speed limit is one standard deviation above the mean speed. For ease of drivers, this will be rounded down to an integer.

Included is a graph of traffic over time, showing traffic jams, as well as our recommendation for the speed limit.
Second is a graph of car position vs time for each car to show the traffic jams as they happen.

requirements.txt -- file contains necessary libraries to run 'traffic900.py' and 'Road-Rage.ipynb.'
Road-Rage.ipynb -- contains visual representation of our findings from 'traffic900.py.'
traffic900.py -- file contains code to run traffic simulation with assumptions listed above.
