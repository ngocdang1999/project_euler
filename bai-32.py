from digits import is_pandigital
from math import log10

def find_pandigital_products():
    result = set()
    
    for a in range(1, 9999):
        for b in range(a, 9999):
            x = a*b
            string = str(a) + str(b) + str(x)
            if len(string) > 9:
                break
            if is_pandigital(string, 9):
                print a, 'x', b, '=', x
                result.add(x)
    return result

if __name__ == '__main__':
    products = find_pandigital_products()
    print 'Sum of pandigital products:', sum(products)
