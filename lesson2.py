#Task - 1
import this
import codecs

zen_of_python = codecs.encode(this.s, 'rot13')

print('''
      ''')

count_better = zen_of_python.count('better')
print ("number of occurrences 'better' - {}".format(count_better))

count_never = zen_of_python.count('never')
print ("number of occurrences 'never' - {}".format(count_never))

count_is = zen_of_python.count('is')
print ("number of occurrences 'is' - {}".format(count_is))

zen_upper = zen_of_python.upper()
print('''
      ''')
print ("zen upper:")
print (zen_upper)

zen_replace = zen_of_python.replace('i','&')
print('''
      ''')
print ("zen replace 'i' -> '&':")
print (zen_replace)



#Task - 2
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



#Task - 3
x = int(input("x: "))
y = int(input("y: "))

x = x + y
y = x - y
x = x - y

print ("x = {}".format(x))
print ("y = {}".format(y))
