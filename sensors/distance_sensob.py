from sensors.sensob import Sensob

# Returns the distance in cm read from the ultrasonic sensor
# Initialized with a single ultrasonic sensor
class DistanceSensob(Sensob):

    def update(self):
        self.value = self.sensors[0].get_value()