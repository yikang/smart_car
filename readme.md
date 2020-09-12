This is ROS packages to test remote Car with Camera

## Setup 

### Hardware: 
refer to hardware.md for hardware setup 

### Software development env: 
```
cd ~/catkin_ws/src
ln -s <path/to/car_bar> car_base
catkin_make 
```

## Usage 

```
# start nodes to listen command 
rosrun car_base move_car.py 

# pushlish command
rostopic pub /rc_command std_msgs/String "wwwwss"
```


