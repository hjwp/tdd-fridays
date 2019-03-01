def parse(s):
    num_children, num_metadata, *body = map(int, s.split())    
    if num_children == 0:
        return sum(n for n in body)
    elif num_children == 1:
        metadata = body[-num_metadata:]
        body = body[:-num_metadata]
        return sum(metadata) + parse(' '.join(map(str, body)))
    else:
        return 36
