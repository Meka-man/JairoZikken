#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor


mst = MoveSteering(OUTPUT_A, OUTPUT_B)
cs1 = ColorSensor(INPUT_1)
cs2 = ColorSensor(INPUT_2)

p = 0
i = 0
d = 0
sta = 0



while True:
    csl = cs1.reflected_light_intensity
    csr = cs2.reflected_light_intensity
    print("main")
    p = csl - csr
    i = p + i
    d = p - d
    sta = p*2 + i*0 + d*0.2
    if sta > 100:
        sta = 100
    elif sta < -100:
        sta = -100
    mst.on(sta, 30)
