def add(first, second):
    smooshed = ''.join(reversed(sorted(f"{first}{second}")))
    result = smooshed.replace('IIIII', 'V').replace('VV', 'X').replace("XXXXX", "L")

    return result
