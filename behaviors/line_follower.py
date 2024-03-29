from behaviors.behavior import Behavior
from motob import Command


class LineFollower(Behavior):
    last_error = 0
    last_value = .5
    SPEED = 0.8
    SPEED_FORWARD = 0.4
    first_tick = True

    kp = 1.6
    kd = 2.0

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)

    def consider_deactivation(self):
        if self.bbcon.line_finished:
            self.bbcon.deactivate_behavior(self)

    def sense_and_act(self):
        if self.first_tick:
            self.first_tick = False
            self.match_degree = 1
            self.motor_recommendations = [(Command.F, self.SPEED_FORWARD)]
            return

        value = self.sensobs[0].get_value()
        print("Line pos:", value)

        if value == -1:
            #self.bbcon.line_finished = True
            #self.bbcon.deactivate_behavior(self)
            self.match_degree = 0
            return

        error = value - 0.5
        pid = self.kp * error + self.kd * (error - self.last_error)
        self.last_error = error

        if abs(pid) > 1:
            pid /= abs(pid)

        print("PID:", pid)

        #self.match_degree = abs(pid) / ((self.kp + self.kd) * 0.5)
        self.match_degree = 1

        if abs(pid) < 0.1:
            self.motor_recommendations = [(Command.F, self.SPEED_FORWARD)]
        else:
            self.motor_recommendations = [(Command.R, self.SPEED * pid)]

        '''if pid < -0.5:
            self.motor_recommendations = [(Command.L, self.SPEED * pid)]
        elif pid > 0.5:
            self.motor_recommendations = [(Command.R, self.SPEED * pid)]
        else:
            self.motor_recommendations = [(Command.F, self.SPEED_FORWARD)]'''