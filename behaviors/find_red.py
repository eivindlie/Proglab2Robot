from behaviors.behavior import Behavior
from motob import Command

class FindRed(Behavior):

    act_count = 0
    last_count_state = "activated"

    def consider_deactivation(self):
        if self.bbcon.sensobs['line_pos'].get_value() != -1:

            if self.last_count_state == "deactivated":
                self.last_count_state = "activated"
                self.act_count = 1
            else:
                self.act_count += 1

            if self.act_count > 2:
                self.bbcon.deactivate_behavior(self)
                self.bbcon.deactivate_sensob(self.bbcon.sensobs['red_search'])
                self.bbcon.deactivate_sensor(self.bbcon.sensors['camera'])


    def consider_activation(self):
        if self.bbcon.sensobs['line_pos'].get_value() == -1:
            if self.last_count_state == "activated":
                self.last_count_state = "deactivated"
                self.act_count = 1
            else:
                self.act_count += 1
            if self.act_count > 7:
                self.bbcon.activate_behavior(self)
                self.bbcon.activate_sensob(self.bbcon.sensobs['red_search'])
                self.bbcon.activate_sensor(self.bbcon.sensors['camera'])


    def sense_and_act(self):
        value = self.sensobs[0].get_value()
        distance = self.sensobs[1].get_value()

        if value == -1:
            print("No red")
            self.motor_recommendations = [(Command.R, 0.3)]
            self.match_degree = 1
        else:
            print("Find red value: ", value)
            if distance < 15:
                print("Finished")
                self.request_halt = True
            if value < 0.4:
                self.motor_recommendations = [(Command.L, 0.3)]
                self.match_degree = 1
            elif value > 0.6:
                self.motor_recommendations = [(Command.R, 0.3)]
                self.match_degree = 1
            else:
                self.motor_recommendations = [(Command.F, 0.3)]
                self.match_degree = 1