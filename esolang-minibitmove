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
