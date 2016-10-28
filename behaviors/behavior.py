

class Behavior:
    bbcon = None
    sensobs = []
    motor_recommendations = []
    active = False
    request_halt = False
    priority = 0
    match_degree = 0


    # Initializes the behavior
    # bbcon: Pointer to the BBCON object that owns this behavior
    # priority: The priority assigned to this behavior. Used to calculate the weight.
    # sensobs: A list of all the sensobs necessary for this behavior to function
    # active: A flag that indicates whether or not this behavior is currently active. (Default: False)
    def __init__(self, bbcon, priority, sensobs, active = False):
        self.bbcon = bbcon
        self.priority = priority
        self.sensobs = sensobs
        self.active = active

    # Tests whether the behavior should deactivate
    def consider_deactivation(self):
        pass

    # Tests whether the behavior should activate
    def consider_activation(self):
        pass

    # Updates the current state of the behavior
    def update(self):
        if self.active:
            self.consider_deactivation()
        else:
            self.consider_activation()
        self.sense_and_act()

    # Reads sensory input, and updates motor recommendations and match degree
    def sense_and_act(self):
        pass

    # Calculates and returns the weight of the behavior
    def get_weight(self):
        return self.priority * self.match_degree