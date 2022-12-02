import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SimpleSubscriber(Node):

    def __init__(self):
        super().__init__('ROS_2_WS')
        self.subscription = self.create_subscription(String, 'ros2_ws', self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Uczestnik/Grupa {msg.data} wpisany')


def main(args=None):
    rclpy.init(args=args)

    simple_subscriber = SimpleSubscriber()

    rclpy.spin(simple_subscriber)

    simple_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
