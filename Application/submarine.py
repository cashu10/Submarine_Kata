class Submarine:
    def __init__(self, depth=0, horizontal=0, aim=0):
        self.depth = depth
        self.horizontal = horizontal
        self.aim = aim

    def moveHorizontal(self, distance, aim=0):
        self.horizontal += distance
        self.depth += self.aim * distance

    def moveDepth(self, distance):
        self.depth += distance

    def moveAim(self, distance):
        self.aim += distance

    def getPosition(self):
        return self.horizontal * self.depth