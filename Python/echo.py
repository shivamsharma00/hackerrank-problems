#!/usr/bin/env python

# importing necessary libraries
import rospy
# from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2



# callback function
def callback_func(data):
    pc = pc2.read_points(data, skip_nans=True, field_names=('x', 'y', 'z'))
    pc_list = []
    for p in pc:
        pc_list.append([p[0], p[1], p[2]])
    print(pc_list)

    
def client_func():
    # creating ROS node
    rospy.init_node('ZED_camera', anonymous=True)
    # creating a subscriber for ZED camera images
    rospy.subscriber('/zed/point_cloud/cloud_registered', PointCloud2, callback_func)
    # initializing ros 
    rospy.spin()

if __name__ == '__main__':
    try:
        client_func()
    except KeyboardInterrupt as e:
        print("Program Interrupted!")
