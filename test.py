import wiringpi2 as wp

import time

from sensors.distance_sensob import DistanceSensob
from sensors.line_pos_sensob import LinePosSensob
from sensors.proximity_sensob import ProximitySensob
from sensors.red_search_sensob import RedSearchSensob

from motob import Motob, Command
from motors import Motors

from sensors.ultrasonic import Ultrasonic
from sensors.camera import Camera
from sensors.reflectance_sensors import ReflectanceSensors
from sensors.irproximity_sensor import IRProximitySensor

def main():
    wp.wiringPiSetupGpio()

    motors = Motors()
    motors.stop()
    motob = Motob(motors)

    sensors = {
        #'ultrasonic': Ultrasonic(0.05),
        #'IR': IRProximitySensor(),
        #'reflectance': ReflectanceSensors(False, 0, 900),
        #'camera': Camera(),
    }

    # Initialize sensobs

    sensobs = {
        #'distance': DistanceSensob([sensors['ultrasonic']]),
        #'line_pos': LinePosSensob([sensors['reflectance']]),
        #'proximity': ProximitySensob([sensors['IR']]),
        #'red_search': RedSearchSensob([sensors['camera']]),
    }

    commands = [(Command.F, 0.5), (Command.F, 1)]
    i=0
    while True:
        for sensor in sensors.values():
            sensor.update()

        for sensob in sensobs.values():
            sensob.update()

        motob.update(commands[i%len(commands)])

        time.sleep(1)
        i+=1

if __name__ == "__main__":
    main()