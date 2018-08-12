#https://www.codewars.com/kata/smart-traffic-lights
i = 0
class SmartTrafficLight():
    def __init__(self, st1, st2):
        global i
        i = 0
        self.st1, self.st2 = st1, st2
    def turngreen(self):
        global i
        if i == 0:
            i += 1
            return self.st1[1] if self.st1[0] > self.st2[0] else (self.st2[1] if self.st1[0] < self.st2[0] else None)
        elif i == 1:
            i += 1
            return self.st1[1] if self.st1[0] < self.st2[0] else (self.st2[1] if self.st1[0] > self.st2[0] else None)
        else:
            return None
