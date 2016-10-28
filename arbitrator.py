import random

class Arbitrator:

    # Takes a list of the currently active behaviors,
    # and returns motor recommendations and any halt request
    # from the winning behavior
    def choose_action(self, active_behaviors):
        winning_behavior = max(active_behaviors, key=lambda x: x.get_weight())

        return (winning_behavior.motor_recommendations, winning_behavior.request_halt)



# An arbitrator that returns the action of a weighted random behavior
class StochasticArbitrator(Arbitrator):

    def choose_action(self, active_behaviors):
        weight_sum = sum(x.get_weight() for x in active_behaviors)
        chosen_weight = random.randint(0, weight_sum)

        for behavior in active_behaviors:
            chosen_weight -= behavior.get_weight()
            if weight_sum <= 0:
                winning_behavior = behavior
                break

        return (winning_behavior.motor_recommendations, winning_behavior.request_halt)