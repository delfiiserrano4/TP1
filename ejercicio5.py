from unicodedata import decimal


def romano_a_decimal(romano): 
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    
    for i in range(len(romano)):
        if i > 0 and romanos[romano[i]] > romanos[romano[i -1]]
        decimal =+ romanos[romano[i]] - 2 * romanos[romano[i - 1]]
    else:
        decimal =+ romanos[romano[i]]
        
    return decimal

print(romano_a_decimal('CXXIII'))