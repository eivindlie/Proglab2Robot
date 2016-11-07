import time
import sys
from motob import Motob
from motors import Motors
from arbitrator import Arbitrator

from sensors.distance_sensob import DistanceSensob

from sensors.ultrasonic import Ultrasonic
from sensors.camera import Camera
from sensors.reflectance_sensors import ReflectanceSensors
from sensors.irproximity_sensor import IRProximitySensor

class BBCON:
    behaviors = []
    active_behaviors = []
    sensors = []
    sensobs = []
    motobs = []
    arbitrator = None

    _wait_duration = 0.5 # The amount of time (in seconds) that the program sleeps each time tick

    def __init__(self):
        # Initialize arbitrator
        self.arbitrator = Arbitrator()

        # Initialize motobs (single object for both motors on the Zumo)
        self.motobs.append(Motob(Motors()))

        # Initialize sensors
        self.sensors.append(Ultrasonic(0.05))
        self.sensors.append(IRProximitySensor())
        self.sensors.append(ReflectanceSensors())
        self.sensobs.append(Camera())

        # Initialize sensobs
        self.sensobs.append(DistanceSensob([self.sensors[0]]))



    def add_behavior(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)
            behavior.active = True

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
            behavior.active = False

    def run_one_timestep(self):
        for sensor in self.sensors:
            sensor.update()

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

        time.sleep(self._wait_duration)

        for sensob in self.sensobs:
            sensob.reset()