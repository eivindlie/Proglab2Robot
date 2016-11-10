from behaviors.behavior import Behavior
from motob import Command

class LineFollower(Behavior):
    last_error = 0
    last_value = .5
    SPEED = 0.4
    first_tick = True

    kp = 0.7
    kd = 4

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)


    def consider_deactivation(self):
        if self.bbcon.line_finished:
            self.bbcon.deactivate_behavior(self)

    def sense_and_act(self):
        if self.first_tick:
            self.first_tick = False
            self.match_degree = 0.5
            self.motor_recommendations = [(Command.F, 0.2)]

        value = self.sensobs[0].get_value()

        if value == -1:
            self.bbcon.line_finished = True
            self.bbcon.deactivate_behavior(self)
            return

        error = value - 0.5
        pid = self.kp * error + self.kd * (error - self.last_error)
        print(pid)

        self.match_degree = abs(pid) / ((self.kp + self.kd) * 0.5)

        if pid < -0.5:
            self.motor_recommendations = [(Command.L, self.SPEED)]
        elif pid > 0.5:
            self.motor_recommendations = [(Command.R, self.SPEED)]
        else:
            self.match_degree = 0.5
            self.motor_recommendations = [(Command.F, 0.2)]