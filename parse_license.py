def parse(s):
    children, metadata, *numbers = s.split()
    if children == '0':
        counter = 0
        for n in numbers:
            counter += int(n)
        return counter
    else:
        return 18
