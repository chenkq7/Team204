#include <ros/ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/String.h>
#include <std_msgs/Int32.h>
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>

static ros::Publisher vel_pub;
static ros::Subscriber sub_sr; 
bool lock;
geometry_msgs::Twist Move_and_turn(double x, double z)
{
    geometry_msgs::Twist vel_cmd;
    vel_cmd.linear.x = x;
    vel_cmd.linear.y = 0;
    vel_cmd.linear.z = 0;
    vel_cmd.angular.x = 0;
    vel_cmd.angular.y = 0;
    vel_cmd.angular.z = z;
    return vel_cmd;
}

geometry_msgs::Twist Stop()
{
    geometry_msgs::Twist vel_cmd;
    vel_cmd.linear.x = 0;
    vel_cmd.linear.y = 0;
    vel_cmd.linear.z = 0;
    vel_cmd.angular.x = 0;
    vel_cmd.angular.y = 0;
    vel_cmd.angular.z = 0;
    return vel_cmd;
}

void move_action(const std_msgs::Float32MultiArray::ConstPtr & msg)
{
float speed, turn;
 geometry_msgs::Twist vel_cmd;

speed = msg->data.at(0);
turn = msg->data.at(1);
if (speed > 0.5)
{
  speed = 0.5;
  ROS_INFO("linear speed warning");
}

if (speed < -0.5)
{
  speed = -0.5;
  ROS_INFO("linear speed warning");
}

if (turn > 0.5)
{
  turn = 0.5;
  ROS_INFO("angular speed warning");
}

if (turn < -0.5)
{
  turn = -0.5;
  ROS_INFO("angular speed warning");
}

if(lock && speed > 0)
{
  speed = 0;
}
  vel_cmd = Move_and_turn(speed, turn*0.3);
  //printf("rec %f, %f\n", speed, turn);
  vel_pub.publish(vel_cmd);
   ros::spinOnce();
}

void move_ctrl(const std_msgs::Int32::ConstPtr & msg)
{
   if (msg -> data == 0)
   {
      lock = false;
   }
   else
   {
     lock = true;
   }
}

int main(int argc, char** argv)
{
  bool lock = false;
    ROS_INFO("move_vel  start\n");
  ros::init(argc, argv, "move_vel");
  ros::NodeHandle n;
  vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
  ros::Subscriber sub = n.subscribe("/move_lock", 10, move_ctrl);
  sub_sr = n.subscribe("/move_vel", 10, move_action);

ros::Rate r(10);
while(ros::ok()){
  ros::spinOnce();
  r.sleep();
}
return 0;
}