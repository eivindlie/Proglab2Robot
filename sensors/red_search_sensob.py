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
                if r > 220 and g < 75 and b < 75:
                    sum += x
                    num += 1

        print("dtime: ", time.time() - self.last_time)
        self.last_time = time.time()

        if num < 0.05 * w * h: # Less than 5 % of the pixels are considered red
            print("Not enough red")
            return -1

        print((sum/num) / w)
        return (sum / num) / w