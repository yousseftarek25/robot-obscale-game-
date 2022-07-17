Modules requirement
from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor,LandmarkMap add 2D visuals, enable animation, contol of vehicle movment across grid, obstacles, and sensor from math import pi, atan2 all math modules import matplotlib.pyplot as plt import numpy as np import sympy plotting added and other math modules

User enter the inputs
Xcoord = int(input("Enter the X coordinate for the robot's starting position: ")) Ycoord = int(input("Enter the Y coordinate for the robot's starting position: ")) obs = int(input("Enter the number of obstacles: ")) Xtarget = int(input("Please enter initial X coordinate to each the goal: ")) Ytarget = int(input("Please enter initial Y coordinate to reach the goal: ")) user chooses start and target coordinates as well as number of obstacles


Desgin and choosing locations
vehicle png chosen and size anim = VehicleIcon('robot1.png', scale = 4)
initlal positon and controlling vehicle movment veh = Bicycle( animation = anim, control = RandomPath, dim = 20, map size x0=(initialPos[0],initialPos[1],0), )
marker size, color, and shape goal_marker_style = { 'marker': ‘E’, 'markersize': 8, 'color': ‘b’, }

Loops
loop does not end until target is reached loop does not start unless parameters are met run=true while(run): for i in sensor.h(veh.x): if (i[0] > 0.5) and (abs(i[1]) > opi): veh.step(1,steer) steer = goal_heading-veh.x[2] plt.pause(0.05) else: veh.step(-1,0) plt.pause(0.05) veh._animation.update(veh.x)
meausers readings of sensor for distance and angle for i in sensor.h(veh.x): dis_land = i[0] ang_land = i[1]

Plotting
plot vehicle and target plt.plot(goal[0], goal[1], **goal_marker_style)
inserting goal inside array goal_array=[goal] goal_array.append(goal) goal_array.insert(0,initialPos) x_array=[item[0] for item in goal_array] y_array=[item[1] for item in goal_array]
