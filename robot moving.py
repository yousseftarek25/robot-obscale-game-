from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor,LandmarkMap
import math
import matplotlib.pyplot as plt

d1 = int(input('please enter the starting x-coordinate:'))
# user input the x coordinaties
e1 = int(input('please enter the starting y-coordinate:'))
# user input the y coordinaties
# user input the z coordinaties
f1 = int(input('please enter the starting z-coordinate:'))
o1 = int(input('lease enter the number of obstacles:'))
# user enter number of obstacles
animat = VehicleIcon('Robot.png', scale = 2)
# robot png uploaded
veh = Bicycle(
 animation=animat,
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
sensor=RangeBearingSensor(robot=veh, map= map ,animate=True)
#  rangebearing sensor for sensing near obstacles 

run =True
while(run):
 goal_heading = atan2(
 goal[1] - veh.x[1],
 goal[0] - veh.x[0]
 )
 steer = goal_heading-veh.x[2]
 veh.step(2,steer)
 if( (abs(goal[0]-veh.x[0]) > 0.5) or (abs(goal[1]-veh.x[1]) >
 0.5) ):
    run=True
 else:
    run =False
 veh._animation.update(veh.x)
 plt.pause(0.003)
#Run robot  for interval seconds
veh._animation.update(veh.x)
plt.pause(1000)
