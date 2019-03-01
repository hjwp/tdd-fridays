def parse(s):
    children, metadata, *numbers = s.split()
    counter = 0
    for n in numbers:
        counter += int(n)
    return counter