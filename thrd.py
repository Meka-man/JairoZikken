#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B,  Motor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

from lib.pid import PIDpulo
import os
from time import sleep

os.system("setfont Vietnamese-Fixed13")
MOVE_ST = MoveSteering(OUTPUT_A, OUTPUT_B)
C_SENSOR1 = ColorSensor(INPUT_1)
C_SENSOR2 = ColorSensor(INPUT_2)
G_Sensor = GyroSensor(INPUT_3)
L_Motor = Motor(OUTPUT_A)
R_Motor = Motor(OUTPUT_B)

PID = PIDpulo(C_SENSOR1, C_SENSOR2, MoveSteering)

while True:
    C_SensorL = C_SENSOR1.reflected_light_intensity
    C_SensorR = C_SENSOR2.reflected_light_intensity
    G_sen = G_Sensor.angle
                                             #PID制御。右からPゲイン、Ⅰゲイン、Ⅾゲイン
    ster = PID.math_pid(C_SensorL, C_SensorR, 2.3, 0, 0)

    if abs(C_SensorL - C_SensorR) > 30:
        if (C_SensorL - C_SensorR) < 0:
            print("Right")
            
            MOVE_ST.on_for_degrees(0, 50, 5)
            
            while C_SensorR > 7:
                C_SensorR = C_SENSOR2.reflected_light_intensity
                L_Motor.on(-30)
                R_Motor.on(30)

        elif (C_SensorL - C_SensorR) > 0:
            print("Left")
            
            MOVE_ST.on_for_degrees(0, 50, 5)
            
            while C_SensorL > 7:
                C_SensorL = C_SENSOR1.reflected_light_intensity
                L_Motor.on(30)
                R_Motor.on(-30)
        
        L_Motor.off()
        R_Motor.off()
        MOVE_ST.off() 
        # sleep(1)
        sterSpd = 11

        print("tyousei")  
        while abs(sterSpd) > 10:
            # MOVE_ST.off()
            # sleep(0.5)
            C_SensorL = C_SENSOR1.reflected_light_intensity
            C_SensorR = C_SENSOR2.reflected_light_intensity
            sterSpd = (C_SensorL-C_SensorR)*1
            MOVE_ST.on(100, sterSpd)
            print(sterSpd)
        MOVE_ST.off() 
        print("fin")
    else:
        if ster < -100:
            ster = -100
        elif ster > 100:
            ster = 100

        MOVE_ST.on(ster, 20)
        # print("GOOOOO")


