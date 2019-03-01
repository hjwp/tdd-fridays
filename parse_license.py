def parse(s):
    num_children, num_metadata, *body = map(int, s.split())
    if num_children == 0:
        return sum(n for n in body)
    metadata = body[-num_metadata:]
    children = body[:-num_metadata]
    if num_children == 1:
        return sum(metadata) + parse(' '.join(map(str, children)))

    else:
        counter = sum(metadata)
        while children:
            child_sum, children = do_a_child(children)
            counter += child_sum
        return counter

def do_a_child(nums):
    return n, unparsed_bits
