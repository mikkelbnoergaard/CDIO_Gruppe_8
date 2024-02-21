#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
test_motor = Motor(Port.B)
test_motor1 = Motor(Port.A)
test_arm=Motor(Port.C)
robot = DriveBase(test_motor,test_motor1, wheel_diameter= 55.5,axle_track=120)

# Write your program here

# Play a sound.
ev3.speaker.beep()

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_arm.run(-500)
robot.straight(500)
test_arm.run_target(500,10000)

# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)
