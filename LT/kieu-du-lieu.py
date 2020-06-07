a = 4
print(a)
print(type(a))

b=9.6
print("gia tri = ", b)
print(type(b))

from decimal import Decimal , getcontext

getcontext().prec =30
c = Decimal(10)/Decimal(3)
print(c)
print(type(c))

from fractions import Fraction
e = Fraction(3,2)
print(e)
print(type(e))
f = e*2
print(f)

