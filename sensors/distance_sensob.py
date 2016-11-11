from sensors.sensob import Sensob

# Returns the distance in cm read from the ultrasonic sensor
# Initialized with a single ultrasonic sensor
class DistanceSensob(Sensob):

    def __init__(self, sensors, threshold = 15):
        super().__init__(sensors)
        self.threshold = threshold

    def update(self):
        self.value = self.sensors[0].get_value()
        print("Distance:", self.value)

    def wall_detected(self):
        return self.value < self.threshold