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
