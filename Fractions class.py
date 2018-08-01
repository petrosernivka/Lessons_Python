def ident_denoms(num1, num2):
    min_num = min(num1, num2)
    while min_num:
        if num1 % min_num == 0 and num2 % min_num == 0 and min_num > 1:
            num1 = num1 / min_num
            num2 = num2 / min_num
            min_num = min(num1, num2)
        else:
            min_num -= 1
    return int(num1), int(num2)

class Fraction:
    
    def __init__(self, numerator, denominator):
        numerator, denominator = ident_denoms(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator
        
    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denominator)
        
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
        
    def __add__(self, other):
        numerator_new = self.numerator * other.denominator + other.numerator * self.denominator
        denominator_new = self.denominator * other.denominator
        return str(Fraction(numerator_new, denominator_new))
