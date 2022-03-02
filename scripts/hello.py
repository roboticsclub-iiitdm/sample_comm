#!/usr/bin/python3

import rospy


if __name__ == '__main__':
	rospy.init_node('hello_py')

	rospy.loginfo("Hello world!")