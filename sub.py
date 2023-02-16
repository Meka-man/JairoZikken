#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, MoveSteering
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import GyroSensor

from lib.mybr import Gyro

G_SENSOR = GyroSensor(INPUT_3)
MOTOR_L = LargeMotor(OUTPUT_A)
MOTOR_R = LargeMotor(OUTPUT_B)
STEERING = MoveSteering(OUTPUT_A, OUTPUT_B)

G_SENSOR.reset()
GYRO = Gyro(G_SENSOR, MOTOR_L, MOTOR_R)

GYRO.rotate(-30)
GYRO.run()