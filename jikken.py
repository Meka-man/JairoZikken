#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B,  Motor
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor

C_sen1 = ColorSensor(INPUT_1)
C_sen2 = ColorSensor(INPUT_2)
A_Motor  = Motor(OUTPUT_A)
B_Motor = Motor(OUTPUT_B)
Move_Str = MoveSteering(OUTPUT_A, OUTPUT_B)
spd = 6

while abs(spd)  > 5: 
    L_cen = C_sen1.reflected_light_intensity
    R_cen = C_sen2.reflected_light_intensity
    spd = L_cen - R_cen
    Move_Str.on(100, spd)