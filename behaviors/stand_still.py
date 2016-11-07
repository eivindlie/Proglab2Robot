from behaviors.behavior import Behavior
from motob import Command

class StandStill(Behavior):

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)
        self.motor_recommendations.append((Command.S))
        self.match_degree = 1

    def sense_and_act(self):
        pass