class Gyro: 
    def __init__(self, G_SENSOR, MOTOR_L, MOTOR_R):
        self.G_SENSOR = G_SENSOR
        self.MOTOR_L = MOTOR_L
        self.MOTOR_R = MOTOR_R


    def rotate(self, TO_ROTATE):
        j = 0

        while j < abs(TO_ROTATE):
            print("sub.py")
            j = self.G_SENSOR.angle
            spd = (TO_ROTATE-j)*50/abs(TO_ROTATE)
            self.MOTOR_L.on(spd)
            self.MOTOR_R.on(-spd)

    def run(self):
        self.MOTOR_R.on(30)
