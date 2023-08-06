class Location:
    # Location class for missionary Cannibal problem
    def __init__(self, name, humans, monsters, capacity):
        self.humans = humans
        self.monsters = monsters
        self.name = name
        self.capacity = capacity

    def increase_human(self):
        if self.capacity == self.size():
            return
        self.humans += 1

    def size(self):
        return self.humans + self.monsters

    def increase_monster(self):
        if self.capacity == self.size():
            return
        self.monsters += 1

    def decrease_human(self):
        if self.humans == 0:
            return
        self.humans -= 1

    def decrease_monster(self):
        if self.monsters == 0:
            return
        self.monsters -= 1

    def is_condition_met(self):
        if self.humans >= self.monsters or (self.humans == 0 and self.monsters > 1):
            return True
        else:
            return False

    def __str__(self):
        return str(self.humans) + " " + str(self.monsters) + " " + str(self.size())
