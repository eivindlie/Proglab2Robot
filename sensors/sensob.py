
class Sensob:
    sensors = []
    value = 0

    def __init__(self, sensors):
        self.sensors = sensors

    # Fetch sensor values, and update the value field correspondingly
    def update(self):
        self.value = 0

    # Return the sensob value
    def get_value(self):
        return self.value

    # Resets value of self and associated sensors
    def reset(self):
        self.value = 0
        for s in self.sensors:
            s.reset()
