#https://www.codewars.com/kata/plotting-points-on-a-grid
class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = ('0' * self.width + '\n') * (self.height -1) + '0' * self.width
    def plot_point(self, x, y):
        self.x = x
        self.y = y
        self.grid = self.grid[:(self.y - 1) * (self.width + 1) + self.x - 1] + 'X' + self.grid[(self.y - 1) * (self.width + 1) + self.x:]
    def __repr__(self):
        return self.grid
