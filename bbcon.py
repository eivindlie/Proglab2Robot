import time
import sys
from motob import Motob
from motors import Motors
from arbitrator import Arbitrator

from sensors.distance_sensob import DistanceSensob
from sensors.line_pos_sensob import LinePosSensob
from sensors.proximity_sensob import ProximitySensob
from sensors.red_search_sensob import RedSearchSensob

from sensors.ultrasonic import Ultrasonic
from sensors.camera import Camera
from sensors.reflectance_sensors import ReflectanceSensors
from sensors.irproximity_sensor import IRProximitySensor

class BBCON:
    behaviors = []
    active_behaviors = []
    sensors = {}
    active_sensors = []
    sensobs = {}
    active_sensobs = []
    motobs = []
    arbitrator = None

    line_finished = False

    _wait_duration = 0.1 #  The amount of time (in seconds) that the program sleeps each time tick

    def __init__(self):
        # Initialize arbitrator
        self.arbitrator = Arbitrator()

        # Initialize motobs (single object for both motors on the Zumo)
        self.motobs.append(Motob(Motors()))

        # Initialize sensors

        self.sensors = {
            'ultrasonic': Ultrasonic(0.05),
            'IR': IRProximitySensor(),
            'reflectance': ReflectanceSensors(False, 0, 900),
            'camera': Camera(),
        }

        self.active_sensors = [self.sensors['ultrasonic'], self.sensors['IR'], self.sensors['reflectance']]


        # Initialize sensobs

        self.sensobs = {
            'distance': DistanceSensob([self.sensors['ultrasonic']]),
            'line_pos': LinePosSensob([self.sensors['reflectance']]),
            'proximity': ProximitySensob([self.sensors['IR']]),
            'red_search': RedSearchSensob([self.sensors['camera']]),
        }

        self.active_sensobs = [self.sensobs['distance'], self.sensobs['line_pos'], self.sensobs['proximity']]

        time.sleep(1)



    def add_behavior(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)
            behavior.active = True

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)
            behavior.active = False

    def activate_sensor(self, sensor):
        if sensor not in self.active_sensors:
            self.active_sensors.append(sensor)

    def deactivate_sensor(self, sensor):
        if sensor in self.active_sensors:
            self.active_sensors.remove(sensor)

    def activate_sensob(self, sensob):
        if sensob not in self.active_sensobs:
            self.active_sensobs.append(sensob)

    def deactivate_sensob(self, sensob):
        if sensob in self.active_sensobs:
            self.active_sensobs.remove(sensob)

    def run_one_timestep(self):
        print("Timestep")
        for sensor in self.active_sensors:
            sensor.update()

        for sensob in self.active_sensobs:
            sensob.update()

        for behavior in self.behaviors:
            behavior.consider_activation()
            behavior.consider_deactivation()

        for behavior in self.active_behaviors:
            behavior.update()

        motor_recommendations, request_halt = self.arbitrator.choose_action(self.active_behaviors)

        if request_halt:
            # If halt is requested: stop all motors, and exit program
            for motob in self.motobs:
                motob.stop()
            sys.exit(0)

        for i in range(len(self.motobs)):
            if len(motor_recommendations) > i:
                self.motobs[i].update(motor_recommendations[i])

        time.sleep(self._wait_duration)

        for sensob in self.sensobs.values():
            sensob.reset()