def roman_number_order(n):
    return 'IVXL'.index(n)


def enforce_simple_rules(roman_number):
    return roman_number.replace('IIIII', 'V').replace('VV', 'X').replace("XXXXX", "L")


def enforce_backwardsey_rules(roman_number):
    return roman_number.replace('VIIII', 'IX').replace('IIII', 'IV')


def add(first, second):
    smooshed = first + second
    ordered = ''.join(reversed(sorted(smooshed, key=roman_number_order)))
    old_style_result = enforce_simple_rules(ordered)
    new_style_result = enforce_backwardsey_rules(old_style_result)
    return new_style_result
