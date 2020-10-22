#include <ros.h> //http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup
#include <std_msgs/String.h>
#include <std_msgs/Float64MultiArray.h>
#include <SpeedyStepper.h> //https://github.com/Stan-Reifel/SpeedyStepper/blob/master/Documentation.pdf

ros::NodeHandle node_handle;

std_msgs::Float64MultiArray axisCommands;
std_msgs::Float64MultiArray joints;

// Connections to driver
const int dirPin1 = 10;  // Direction for axis 1
const int stepPin1 = 9;// Step for axis 1

const int dirPin2 = 7;  // Direction for axis 2
const int stepPin2 = 6; // Step for axis 2

const int dirPin3 = 4;  // Direction for axis 3
const int stepPin3 = 3; // Step for axis 3

float axis_1_pos = 0;
float axis_2_pos = 0;
float axis_3_pos = 0;

SpeedyStepper axis1;
SpeedyStepper axis2;
SpeedyStepper axis3;

ros::Publisher joint_publisher("arduino_publisher", &joints);

void subscriberCallback(const std_msgs::Float64MultiArray &axisCommands) {
  axis_1_pos = axisCommands.data[0];
  axis_2_pos = axisCommands.data[1];
  axis_3_pos = axisCommands.data[2];

  axis1.setupMoveInRevolutions(axis_1_pos);
  axis2.setupMoveInRevolutions(axis_2_pos);
  axis3.setupMoveInRevolutions(axis_3_pos);

  axis1.processMove()
  axis1.processMove()
  axis1.processMove()

  
}

ros::Subscriber<std_msgs::Float64MultiArray> motor_subscriber("axis_commands", &subscriberCallback);

void setup() {
  
  // Setup the steppers with speedy stepper lib
  axis1.connectToPins(stepPin1, dirPin1);
  axis2.connectToPins(stepPin2, dirPin2);
  axis3.connectToPins(stepPin3, dirPin3);

   // set the speed and acceleration rates for the stepper motor
  axis1.setStepsPerRevolution(200);
  axis1.setSpeedInRevolutionsPerSecond(1.0);
  axis1.setAccelerationInRevolutionsPerSecondPerSecond(1.0);
  
  axis2.setStepsPerRevolution(200);
  axis2.setSpeedInRevolutionsPerSecond(1.0);
  axis2.setAccelerationInRevolutionsPerSecondPerSecond(1.0);

  axis3.setStepsPerRevolution(200);
  axis3.setSpeedInRevolutionsPerSecond(1.0);
  axis3.setAccelerationInRevolutionsPerSecondPerSecond(1.0);
  //Limit switch to start point in the future

  Serial.begin(9600);

}
void loop() {

  float joint1 = axis1.getCurrentPositionInRevolutions()
  float joint2 = axis1.getCurrentPositionInRevolutions()
  float joint3 = axis1.getCurrentPositionInRevolutions()
  
  joints.data = {joint1, joint2, joint3};
  joint_publisher.publish( &joints );
  node_handle.spinOnce();

  delay(50);
}