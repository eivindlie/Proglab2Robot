from behaviors.behavior import Behavior
from motob import Command
import time

class RunForward(Behavior):

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)
        self.start_time = time.time()

    def sense_and_act(self):
        if time.time() - self.start_time < 5:
            self.motor_recommendations = [(Command.F, 0.5)]
        else:
            self.request_halt = True
        self.match_degree = 1.0