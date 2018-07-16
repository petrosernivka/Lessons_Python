#https://www.codewars.com/kata/will-you-make-it
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False
    

#https://www.codewars.com/kata/interactive-dictionary
class Dictionary():
    def __init__(self, word = '', definition = ''):
        self.word = word
        self.definition = definition
    def newentry(self, word, definition):
        self.word = word
        self.definition = definition
    def look(self, word):
        return self.definition if self.word == word else '''Can't find entry for ''' + word


#https://www.codewars.com/kata/reversing-words-in-a-string
def reverse(st):
    return ' '.join(reversed(st.split(' ')))


#https://www.codewars.com/kata/how-much-will-you-spend
def getTotal(costs, items, tax):
    for key in items:
        if key not in costs:
            costs[key] = 0
    return round(sum(costs[i] for i in items)*(1+tax),2)


#https://www.codewars.com/kata/noob-debug-1-fix-the-string-sum
def add(s1, s2):
    s1 = s1.encode()
    s2 = s2.encode()
    s1 = sum(s1)
    s2 = sum(s2)
    return s1+s2


#https://www.codewars.com/kata/make-a-square-box
def box(n):
    ar = []
    a = '-'
    ar.append(a * n)
    i = 1
    while i <= (n-2):
        ar.append(a + ' ' * (n-2) + a)
        i += 1
    ar.append(a * n)
    return ar


#https://www.codewars.com/kata/21-sticks
def makeMove(sticks):
    if sticks in (21, 20, 16, 12, 8, 4):
        p = 1
    elif sticks > 16:
        p = sticks - 16
    elif sticks > 12:
        p = sticks - 12
    elif sticks > 8:
        p = sticks - 8
    elif sticks > 4:
        p = sticks - 4
    else:
        p = sticks
    return p


#https://www.codewars.com/kata/pig-atinlay
def pig_latin(word):
    return word if len(word) < 4 else word[1:]+word[0]+"ay"


#https://www.codewars.com/kata/alien-accent
def convert(st):
    return st.replace('o','u').replace('a','o')


#https://www.codewars.com/kata/will-there-be-enough-space
def enough(cap, on, wait):
    return 0 if cap >= on + wait else wait - cap + on


#https://www.codewars.com/kata/no-yelling
def filter_words(st):
    return st.capitalize().replace('  ',' ').replace('  ',' ').strip()


#https://www.codewars.com/kata/simple-find-the-distance-between-two-points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2)**(0.5), 2)


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


#https://www.codewars.com/kata/file-path-operations
class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        return self.filepath[len(self.filepath)-len(self.filepath)+self.filepath.find('.')+1:]
    def filename(self):
        return self.filepath[-len(self.filepath)+self.filepath.rfind('/')+1:-len(self.filepath)+self.filepath.find('.')]
    def dirpath(self):
        return self.filepath[:-len(self.filepath)+self.filepath.rfind('/')+1]


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


#https://www.codewars.com/kata/esolang-minibitmove
def interpreter(tape, array):
    import math
    array_new, x, y = '', 0, 0
    a = (tape * math.ceil(len(array) / tape.count('0'))).split('0')
    
    while x <= len(array) - 1:
        if a[y] == '':
            array_new += array[x]
            x += 1
            y += 1
        else:
            i = 0
            b = array[x]
            while i <= len(a[y]) - 1:
                b = str(abs(int(b)-1))
                i += 1
            array_new += b
            x += 1
            y += 1
  
    return array_new


#https://www.codewars.com/kata/esolang-tick
def interpreter(tape):
    a = tape.split('*')
    i = a.pop()
    count_plus, count_men, nenull, tape_interp = [], [], [], ''

    for i in a:
        count_plus.append(i.count('+'))
        count_men.append(i.count('<'))
    
    x, z = 0, 0
    for i in count_plus:
        if i == 0:
            tape_interp += chr(nenull[z-1-count_men[x]])
        else:
            tape_interp += chr(count_plus[x])
            nenull.append(count_plus[x])
            z += 1
        x += 1
    
    return tape_interp


#https://www.codewars.com/kata/the-modulo-3-sequence
def sequence(n):
    return int('01120221'[n - int(n/8)*8 - 1])
