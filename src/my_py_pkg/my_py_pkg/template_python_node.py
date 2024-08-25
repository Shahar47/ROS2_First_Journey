#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyCoustomNode(Node):

    def __init__(self):
        super().__init__("node_name")
        self.get_logger().info("mode_name has been started.")



def main(args=None):
    rclpy.init(args=args) 
    node = MyCoustomNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()