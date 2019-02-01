
def roman_number_order(n):
    return 'IVXL'.index(n)

def add(first, second):
    smooshed = ''.join(reversed(sorted(f"{first}{second}", key=roman_number_order)))
    result = smooshed.replace('IIIII', 'V').replace('VV', 'X').replace("XXXXX", "L")
    return result
