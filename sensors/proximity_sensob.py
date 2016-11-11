from sensors.sensob import Sensob

# Reads the values from the IR proximity sensors,
# sensors a list of one irproximity_sensor
# Returns a two-boolean tuple, indicating proximity on left and right
class ProximitySensob(Sensob):

    def update(self):
        self.value = self.sensors[0].get_value()
        print(self.value)