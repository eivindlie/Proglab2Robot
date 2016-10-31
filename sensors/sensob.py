
class Sensob:
    sensors = []
    value = 0

    def __init__(self, sensors):
        self.sensors = sensors

    # Fetch sensor values, and update the value field correspondingly
    def update(self):
        self.value = 0