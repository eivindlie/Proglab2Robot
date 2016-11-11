from behaviors.behavior import Behavior
from motob import Command

# Requires 1 distnace sensob as index 0 and 1 proximity sensob as index 1
class AvoidWalls(Behavior):

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)
        self.motor_recommendations.append((Command.F, 0))

    def sense_and_act(self):
        distance = self.sensobs[0].get_value()
        side_proximity = self.sensobs[1].get_value()

        # distnace for ultrasonic sensor to be considered too close
        distance_threshold = 10


        # boolean values for proximity in these directions
        left_side = side_proximity[0]
        right_side = side_proximity[1]
        front = distance < distance_threshold



        if front and not left_side and not right_side:
            self.motor_recommendations[0] = (Command.B, 0.35)
            #self.request_halt = True
            #self.motor_recommendations = [Command.S]
            self.match_degree = 1
        elif left_side:
            self.motor_recommendations[0] = (Command.R, 0.45)
            self.match_degree = 1
        elif right_side:
            self.motor_recommendations[0] = (Command.L, 0.45)
            self.match_degree = 1
        else:
            self.match_degree = 0
            self.motor_recommendations[0] = (Command.S)