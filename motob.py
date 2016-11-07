from enum import Enum

class Motob:

    def __init__(self, motors):
        self.motors = motors
        self.value = None

    def update(self, motor_recommendation):
        self.value = motor_recommendation
        self.operationalize()

    def operationalize(self):
        # convert motor recomendation into motor settings, and send settings to motors
        c = self.value[0]
        if c == Command.F: # Forwards
            self.motors.forward(self.value[1]) # Second parameter in the command is speed
        elif c == Command.B: # Backwards
            self.motors.backward(self.value[1]) # Second parameter in the command is speed
        elif c == Command.L: # Turn left
            self.motors.left(self.value[1])
        elif c == Command.R: # Turn right
            self.motors.right(self.value[1])

    def stop(self):
        self.motors.stop()

class Command(Enum):
    F = 0 # Forward
    B = 1 # Backward
    L = 2 # Turn left
    R = 3 # Turn right