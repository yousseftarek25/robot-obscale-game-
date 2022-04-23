from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor,LandmarkMap
from math import pi, atan2
import matplotlib.pyplot as plt

d1 = int(input('please enter the starting x-coordinate:'))
# user input the x coordinaties
e1 = int(input('please enter the starting y-coordinate:'))
# user input the y coordinaties
f1 = int(input('please enter the starting z-coordinate:'))
# user input the z coordinaties
o1 = int(input('lease enter the number of obstacles:'))
# user enter number of obstacles
anim = VehicleIcon('Robot.png', scale = 2)
# robot png uploaded
veh = Bicycle(
 animation=anim,
 control=RandomPath,
 x0=(d1,e1,f1),
)
veh.init(plot=True)
# initial postion was changes by the user it has to be updated
map = LandmarkMap(o1,20)
# map size +20 or -20 and user input number of obstacles
map.plot()

c2 = int(input('Please enter the target x-coordinate:'))
# user provides the targeted coordinates of x
d2 = int(input('Please enter the target y-coordinate:'))
# user provides the targeted coordinates of y
goal=[c2,d2]; 
goal_marker_style = {
 'marker': 'D',
 'markersize': 6,
 'color': 'b',
}
# target position, size and colour
plt.plot(goal[0], goal[1], **goal_marker_style)
# plot robot and target points
