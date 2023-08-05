class Pokemon:
    def __init__(self, power, level, names):
        self.power = power
        self.level = level
        self.names = names
    def __repr__(self):
        return (f'Pokemon({self.power}, '
                f'{self.level}, '
                f'{self.names})')
 
    def total_damage(self):
        return self.damage(self.power, self.level)
    @staticmethod
    def damage(power, level):
        return (power * level * 2) / 50
        