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
                if r > 2.2*g and r > 2.2*b:
                    sum += x
                    num += 1

        self.last_time = time.time()

        if num < 0.10 * w * h: # Less than 10% of the pixels are considered red
            self.value = -1
            print("Red val: ", self.value)
            return

        self.value = (sum / num) / w
        print("Red val: ", self.value)

    def reset(self):
        super().reset()
        self.value = -1