from sensors.sensob import Sensob

# Takes a reading from the reflectance sensors,
# and gives a position for where a line is underneath the robot.
# This value is between 0 and 5, for all the way to the left to
# all the way to the right, correspondingly.
# If no line is detected, the value is set to -1
class LinePosSensob(Sensob):

    threshold = 0.30 # Threshold for a reading to be considered a line

    def update(self):
        values = self.sensors[0].get_value()
        print(values)

        '''avg = 0
        sum = 0

        for i in range(len(values)):
            value = values[i]

            if value < 0.05:
                avg += (1-value) * i
                sum += (1-value)

        if sum == 0:
            self.value = -1
        else:
            self.value = avg/sum

        print("Line pos", self.value)'''

        pos = 0
        count = 0

        for i in range(len(values)):
            if values[i] < self.threshold
                pos += i
                count += 1
        if count == 0:
            self.value = -1
            return
        self.value = pos/count
        print("Line pos", self.value)