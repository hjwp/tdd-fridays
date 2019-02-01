def roman_number_order(n):
    return 'IVXL'.index(n)

def add(first, second):
    smooshed = first + second
    ordered = ''.join(reversed(sorted(smooshed, key=roman_number_order)))
    old_style_result = ordered.replace('IIIII', 'V').replace('VV', 'X').replace("XXXXX", "L")
    new_style_result = old_style_result.replace('IIII', 'IV')
    return new_style_result
