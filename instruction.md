# Usefull commands
## Kill gazebo server
```bash
kill $(ps -aux | grep gzserver | cut -d" " -f 2)
```

# Instruction
## Step 1
Add to `~/.bashrc` these lines (change `<number>` to your computer number):
```bash
export ROS_DOMAIN_ID=<number>
source /opt/ros/foxy/setup.bash

```
This allows you to use `ros2` commands. 

## Step 2 
Try build and launch empty setup:
```bash
# Building:
colcon build

# Installing :
source install/setup.bash
```

## Step 4
Launch built package:
```bash
ros2 launch robot_description robot.launch.py
```
You should see in the terminal:
```bash
got segment base_link
got segment body_link
```

## Step 5 
Open `rviz2` change fixed frame to `base_link`, display `TF` and click checkbox `Show names`
```bash
rviz2
```

