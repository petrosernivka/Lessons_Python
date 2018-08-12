#https://www.codewars.com/kata/simple-find-the-distance-between-two-points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2)**(0.5), 2)
