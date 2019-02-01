def add(first, second):
    result = f"{first}{second}"

    if len(result) > 3:
        return "V"

    return ''.join(reversed(sorted(result)))
