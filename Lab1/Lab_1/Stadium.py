class Stadium:
    def __init__(self, number_of_viewers, name, power_of_ligthing):
        self.name = name
        self.number = number_of_viewers
        self.power = power_of_ligthing

    def __str__(self):
        return " Name: " + str(self.name) + "; " + \
            " viewers: " + str(self.number) + "; " \
            " power: " + str(self.power) + "; "
