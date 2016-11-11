from behaviors.behavior import Behavior
from motob import Command
import time

class RunForward(Behavior):


    def sense_and_act(self):
        self.motor_recommendations = [(Command.F, 0.4)]
        self.match_degree = 1