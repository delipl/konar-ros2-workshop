# Usefull commands
## Kill gazebo server
```bash
kill $(ps -aux | grep gzserver | cut -d" " -f 2)
```

## Joy
```bash
ros2 launch teleop_twist_joy teleop-launch.py joy_config:='xbox'
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
got segment base_link
```

## Step 5 
Open `rviz2` change fixed frame to `base_link`, display `TF` and click checkbox `Show names`
```bash
rviz2
```

## Step 6
Add robot properites to `urdf`.

```xml
<xacro:property name="base_width" value="0.31"/>
<xacro:property name="base_length" value="0.42"/>
<xacro:property name="base_height" value="0.18"/>
<xacro:property name="base_mass" value="1.0"/>

<xacro:property name="wheel_radius" value="0.10"/>
<xacro:property name="wheel_width" value="0.04"/>
<xacro:property name="wheel_ygap" value="0.025"/>
<xacro:property name="wheel_zoff" value="0.05"/>
<xacro:property name="wheel_xoff" value="0.12"/>
```

## Step 7 
Add property box to `base_link`
```xml
<geometry>
        <box size="${base_length} ${base_width} ${base_height}" />
</geometry>
```

## Step 8
Create wheel macro
```xml
<xacro:macro name="wheel" params="prefix x_reflect y_reflect">
        <link name="${prefix}_link">
            <visual>
                <origin xyz="0 0 0" rpy="${pi/2} 0 0"/>
                <geometry>
                    <cylinder radius="${wheel_radius}" length="${wheel_width}"/>
                </geometry>
                <material name="Gray">
                    <color rgba="0.5 0.5 0.5 1.0"/>
                </material>
            </visual>
            <collision>
                <origin xyz="0 0 0" rpy="${pi/2} 0 0"/> 
                <geometry>
                    <cylinder radius="${wheel_radius}" length="${wheel_width}"/>
                </geometry>
            </collision>
            <xacro:cylinder_inertia m="${wheel_mass}" r="${wheel_radius}" h="${wheel_width}"/>
        </link>

        <joint name="${prefix}_joint" type="continuous">
            <parent link="base_link"/>
            <child link="${prefix}_link"/>
            <origin xyz="${x_reflect*wheel_xoff} ${y_reflect*(base_width/2+wheel_ygap)} ${-wheel_zoff}" rpy="0 0 0"/>
            <axis xyz="0 1 0"/>
        </joint>
</xacro:macro>
```

## Step 9
Added wheels
```xml
<xacro:wheel prefix="drivewhl_l" x_reflect="-1" y_reflect="1" />
<xacro:wheel prefix="drivewhl_r" x_reflect="-1" y_reflect="-1" />
```

## Step 10
Change wheel joint type to `continuous`
## Step 11
Launch `joint_state_publisher_gui`. Return `joint_state_publisher_gui_node` in launch file. 

## Step 12
Add support wheel.
```xml
<!-- Caster Wheel -->
<link name="front_caster">
        <visual>
                <geometry>
                <sphere radius="${(wheel_radius+wheel_zoff-(base_height/2))}"/>
                </geometry>
                <material name="Cyan">
                <color rgba="0 1.0 1.0 1.0"/>
                </material>
        </visual>
        <collision>
                <geometry>
                <sphere radius="${(wheel_radius+wheel_zoff-(base_height/2))}"/>
                </geometry>
        </collision>    
</link>

<joint name="caster_joint" type="fixed">
        <parent link="base_link"/>
        <child link="front_caster"/>
        <origin xyz="${caster_xoff} 0.0 ${-(base_height/2)}" rpy="0 0 0"/>
</joint>
```

## Step 13
Remove friction from caster wheel
```xml
<gazebo reference="front_caster">
        <mu>0.001</mu>
        <mu2>0.001</mu2>
</gazebo>
```

## Step 14
Add diff drive controller
```xml
 <gazebo>
        <plugin name='diff_drive' filename='libgazebo_ros_diff_drive.so'>
            <!-- wheels -->
            <left_joint>drivewhl_l_joint</left_joint>
            <right_joint>drivewhl_r_joint</right_joint>

            <!-- kinematics -->
            <wheel_separation>0.4</wheel_separation>
            <wheel_diameter>0.2</wheel_diameter>

            <!-- limits -->
            <max_wheel_torque>20</max_wheel_torque>
            <max_wheel_acceleration>1.0</max_wheel_acceleration>

            <!-- output -->
            <publish_odom>true</publish_odom>
            <publish_odom_tf>true</publish_odom_tf>
            <publish_wheel_tf>true</publish_wheel_tf>

            <odometry_frame>odom</odometry_frame>
            <robot_base_frame>base_link</robot_base_frame>
        </plugin>
    </gazebo>
```

## Step 15
Add lidar
