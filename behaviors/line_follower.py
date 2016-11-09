from behaviors.behavior import Behavior
from motob import Command
import time

class LineFollower(Behavior):
    last_error = 0
    last_value = .5
    SPEED = 0.35

    kp = 0.5
    kd = 4

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)
        self.start_time = time.time()


    def consider_deactivation(self):
        if self.bbcon.line_finished:
            self.bbcon.deactivate_behavior(self)

    def sense_and_act(self):
        value = self.sensobs[0].get_value()

        if time.time() - self.start_time > 1 and value == -1:
            self.bbcon.line_finished = True
            return

        error = value - 0.5
        pid = self.kp * error + self.kd * (error - self.last_error)

        self.match_degree = pid / ((self.kp + self.kd) * 0.5)
        print(pid)
        if pid < -0.5:
            self.motor_recommendations = [(Command.L, self.SPEED)]
        elif pid > 0.5:
            self.motor_recommendations = [(Command.R, self.SPEED)]
        else:
            self.match_degree = 0.5
            self.motor_recommendations = [(Command.F, 0.3)]