from sensors.sensob import Sensob

# Returns the distance in cm read from the ultrasonic sensor
# Initialized with a single ultrasonic sensor
class DistanceSensob(Sensob):

    def __init__(self, threshold = 15):
        self.threshold = threshold

    def update(self):
        self.value = self.sensors[0].get_value()
        print("distance", self.value)

    def wall_detected(self):
        return self.value < self.threshold