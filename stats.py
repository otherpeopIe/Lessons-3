

class Stat:
    def __init__(self, name, min, max):
        self.name = name
        self. min = min
        self.max = max
        self.value = min

        

    def display(self):
        print(self.name + ": " + str(self.value))

    def setvalue(self, val):
        self.value = val