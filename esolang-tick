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
