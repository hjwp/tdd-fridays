def parse(s):
    num_children, num_metadata, *body = s.split()
    if num_children == '0':
        return sum(int(n) for n in body)
    else:
        return parse(' '.join(body))
