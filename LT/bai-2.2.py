x=int(input("nhap:"))
def facttdang(x):
    if x == 0:
      return 1
    else:
      return x * facttdang(x - 1)
print (facttdang(x))