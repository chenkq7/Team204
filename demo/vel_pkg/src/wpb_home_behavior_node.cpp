/*********************************************************************
* Software License Agreement (BSD License)
* 
*  Copyright (c) 2017-2020, Waterplus http://www.6-robot.com
*  All rights reserved.
* 
*  Redistribution and use in source and binary forms, with or without
*  modification, are permitted provided that the following conditions
*  are met:
* 
*   * Redistributions of source code must retain the above copyright
*     notice, this list of conditions and the following disclaimer.
*   * Redistributions in binary form must reproduce the above
*     copyright notice, this list of conditions and the following
*     disclaimer in the documentation and/or other materials provided
*     with the distribution.
*   * Neither the name of the WaterPlus nor the names of its
*     contributors may be used to endorse or promote products derived
*     from this software without specific prior written permission.
* 
*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
*  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
*  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
*  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
*  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
*  FOOTPRINTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
*  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
*  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
*  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
*  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
*  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
*  POSSIBILITY OF SUCH DAMAGE.
*********************************************************************/
/*!******************************************************************
 @author     ZhangWanjie
 ********************************************************************/

#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>

ros::Publisher vel_pub;

void lidarCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
    int nNum = scan->ranges.size();
    
    
    int nLeft = nNum/4;
    float leftDist = scan->ranges[nLeft];

    int nMid = nNum/2;
    float frontDist = scan->ranges[nMid];
    int nLeftMid = (nMid+nLeft)/2;
    float leftMidDist = scan->ranges[nLeftMid];
    
    int nRight = nLeft+nMid;
    float rightDist = scan->ranges[nRight];
    int nRightMid = (nMid+nRight)/2;
    float rightMidDist = scan->ranges[nRightMid];
    ROS_INFO("Point[%d] = %f,Point[%d] = %f,Point[%d] = %f, Point[%d] = %f,Point[%d] = %f", 
        nLeft, leftDist, nLeftMid, leftMidDist, nMid, frontDist, nRightMid, rightMidDist, nRight, rightDist); 


    geometry_msgs::Twist vel_cmd;
    float dis = 1.5;
    if(frontDist > dis && leftDist > dis && rightDist > dis && leftMidDist > dis && rightMidDist > dis)
    {
        vel_cmd.linear.x = 0.4;
    }
    else
    {
        vel_cmd.angular.z = 0.3;
    }
    vel_pub.publish(vel_cmd);
}

int main(int argc, char** argv)
{
    ros::init(argc,argv,"wpb_home_behavior_node");
    
    ROS_INFO("wpb_home_behavior_node start!");

    ros::NodeHandle nh;
    ros::Subscriber lidar_sub = nh.subscribe("/scan", 10, &lidarCallback);
    vel_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel",10);
    //vel_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel_mux/input/teleop",10);

    ros::spin();
}
