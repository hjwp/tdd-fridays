def make_order(roman_number):
    return ''.join(reversed(sorted(roman_number, key=roman_number_order)))


def roman_number_order(n):
    return 'IVXL'.index(n)


def enforce_simple_rules(roman_number):
    return roman_number.replace('IIIII', 'V').replace('VV', 'X').replace("XXXXX", "L")


def enforce_backwardsey_rules(roman_number):
    return roman_number.replace('VIIII', 'IX').replace('IIII', 'IV')


def convert_to_simple_roman_number(backwardsey_roman_number):
    return backwardsey_roman_number.replace('IV', 'IIII')


def add(first, second):
    first = convert_to_simple_roman_number(first)
    second = convert_to_simple_roman_number(second)
    smooshed = first + second
    ordered = make_order(smooshed)
    old_style_result = enforce_simple_rules(ordered)
    new_style_result = enforce_backwardsey_rules(old_style_result)
    return new_style_result
