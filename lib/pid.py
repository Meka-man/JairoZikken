class PIDpulo:
    def __init__(self, C_SENSOR1, C_SENSOR2, MoveSteering):
        self.C_SENSOR1 = C_SENSOR1
        self.C_SENSOR2 = C_SENSOR2
        self.MoveSteering = MoveSteering

        self.i = 0
        self.d = 0
        
    def math_pid(self, a, b, P_gain, I_gain, D_gain):
        p = a - b
        self.i = p + self.i
        self.d = p - self.d
        return p*P_gain + self.i*I_gain + self.d*D_gain