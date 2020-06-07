import math
c = 50
h = 30
value = []
e =[x for x in input("nhap gia tri cua d: ").split(',')]
for d in e:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(value))