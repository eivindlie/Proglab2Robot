import time
import sys
from motob import Motob
from motors import Motors
from arbitrator import Arbitrator

class BBCON:
    behaviors = []
    active_behaviors = []
    sensobs = []
    motobs = []
    arbitrator = None

    _wait_duration = 0.5 # The amount of time (in seconds) that the program sleeps each time tick

    def __init__(self):
        # Initialize arbitrator
        self.arbitrator = Arbitrator()

        # Initialize motobs (single object for both motors on the Zumo)
        self.motobs.append(Motob(Motors()))

        # Initialize sensobs
        pass



    def add_behavior(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        for sensob in self.sensobs:
            sensob.update()

        for behavior in self.active_behaviors:
            behavior.update()

        motor_recommendations, request_halt = self.arbitrator.choose_action(self.active_behaviors)

        if request_halt:
            # If halt is requested: stop all motors, and exit program
            for motob in self.motobs:
                motob.stop()
            sys.exit(0)

        for i in range(len(motor_recommendations)):
            self.motobs[i].update(motor_recommendations[i])

        time.sleep(self._sleep_duration)

        for sensob in self.sensobs:
            sensob.reset()