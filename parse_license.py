def parse(s):
    num_children, num_metadata, *body = map(int, s.split())
    if num_children == 0:
        return sum(n for n in body)
    metadata = body[-num_metadata:]
    children = body[:-num_metadata]
    
    counter = sum(metadata)
    while children:
        child_sum, children = parse_one(children)
        counter += child_sum
    return counter

def parse_one(nums):
    num_children, num_metadata, *remaining = nums

    if num_children == 0:
        return sum(remaining[:num_metadata]), remaining[num_metadata:]

    counter = 0
    for _ in range(num_children):
        child_sum, remaining = parse_one(remaining)
        counter += child_sum

    metadata = remaining[:num_metadata]
    remaining = remaining[num_metadata:]

    return counter + sum(metadata), remaining
