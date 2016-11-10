from behaviors.behavior import Behavior
from motob import Command
import time

class LineFollower(Behavior):
    last_error = 0
    last_value = .5
    SPEED = 0.40

    kp = 0.5
    kd = 5

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)
        self.start_time = time.time()


    def consider_deactivation(self):
        if self.bbcon.line_finished:
            self.bbcon.deactivate_behavior(self)

    def sense_and_act(self):
        if time.time() - self.start_time < 1:
            return

        value = self.sensobs[0].get_value()

        if value == -1:
            self.bbcon.line_finished = True
            self.bbcon.deactivate_behavior(self)
            return

        error = value - 0.5
        pid = self.kp * error + self.kd * (error - self.last_error)

        self.match_degree = abs(pid) / ((self.kp + self.kd) * 0.5)

        if pid < -0.5:
            self.motor_recommendations = [(Command.L, self.SPEED)]
        elif pid > 0.5:
            self.motor_recommendations = [(Command.R, self.SPEED)]
        else:
            self.match_degree = 0.5
            self.motor_recommendations = [(Command.F, 0.2)]