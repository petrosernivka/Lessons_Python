a = input("4-хзначне число: ")

dobutok = int(a[0])*int(a[1])*int(a[2])*int(a[3])
print ("добуток чисел - {}".format(dobutok))

revers = a[3] + a[2] + a[1] + a[0]
print ("реверсний порядок - {}".format(revers))

i = 4
sort = [a[0], a[1], a[2], a[3]]

while i > 1:
    for j in range(i-1):
        if sort[j] > sort[j+1]:
            k = sort[j]
            sort[j] = sort[j+1]
            sort[j+1] = k
    i -= 1

print ("відсортовані цифри - {}".format(sort))
