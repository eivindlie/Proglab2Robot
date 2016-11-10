from sensors.sensob import Sensob
import time

class RedSearchSensob(Sensob):

    def __init__(self, sensors):
        super().__init__(sensors)
        self.last_time = time.time()

    def update(self):
        image = self.sensors[0].get_value()
        w, h = image.size

        sum = 0
        num = 0

        for y in range(h):
            for x in range(w):
                r, g, b = image.getpixel((x, y))
                if r > 1.8*g and r > 1.8*b:
                    sum += x
                    num += 1

        self.last_time = time.time()

        if num < 0.01 * w * h: # Less than 3% of the pixels are considered red
            self.value = -1
            return

        self.value = (sum / num) / w