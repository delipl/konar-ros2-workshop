from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, LaunchConfiguration
from os import path

package_name = 'robot_description'

def generate_launch_description():
    robot_name="my_robot"
    robot_description_path = FindPackageShare(package=package_name).find(package_name)
    robot_description_urdf_path = path.join(robot_description_path, 'resource/robot.urdf.xacro')
    # world_path=path.join(robot_description_path, 'world/my_world.sdf')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', robot_description_urdf_path])}]
    )

    spawn_robot = Node(
    	package='gazebo_ros', 
    	executable='spawn_entity.py',
        arguments=['-entity', robot_name, '-topic', 'robot_description'],
        output='screen'
    )

    return LaunchDescription([
        # Run Gazebo
        # ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'], output='screen'),
        robot_state_publisher_node,

    ])
