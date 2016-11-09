from behaviors.behavior import Behavior
from motob import Command

class FindRed(Behavior):

    def consider_activation(self):
        if self.bbcon.line_finished:
            self.bbcon.activate_behavior(self)
            self.bbcon.activate_sensob(self.bbcon.sensobs['red_search'])
            self.bbcon.activate_sensor(self.bbcon.sensors['camera'])

    def sense_and_act(self):
        value = self.sensobs[0].get_value()

        if value == -1:
            self.motor_recommendations = [(Command.R, 0.4)]
            self.match_degree = 0.7
        else:
            if value < 0.4:
                self.motor_recommendations = [(Command.L, 0.3)]
                self.match_degree = 0.8
            elif value > 0.4:
                self.motor_recommendations = [(Command.R, 0.3)]
                self.match_degree = 0.8
            else:
                self.motor_recommendations = [(Command.F, 0.4)]
                self.match_degree = 0.8