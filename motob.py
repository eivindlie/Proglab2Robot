class Motob:

    def __init__(self, motors):
        self.motors = motors
        self.value = None

    def update(self, motor_recomendation):
        self.value = motor_recomendation
        self.operationalize()

    def operationalize(self):
        # convert motor recomendation into motor settings, and send settings to motors
        pass

    