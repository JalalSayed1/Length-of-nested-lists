def get_length(lst):
    length = 0
    # base case:
    if len(lst) == 0:
        print(length)
        return length

    for elt in lst:
        if isinstance(elt, list):
            print("elt is a list", length)
            length += int(get_length(elt))
            print(length)
        else:
            print("elt is not a list", length)
            length += 1
            print(length)


get_length([1, [2, 3]])
