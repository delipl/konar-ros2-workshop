from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import Command, LaunchConfiguration
from os import path

package_name = 'robot_description'

def generate_launch_description():
    robot_description_path = FindPackageShare(package=package_name).find(package_name)
    robot_description_urdf_path = path.join(robot_description_path, 'resource/robot.urdf.xacro')

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', robot_description_urdf_path])}]
    )

    return LaunchDescription([
        robot_state_publisher_node
    ])
