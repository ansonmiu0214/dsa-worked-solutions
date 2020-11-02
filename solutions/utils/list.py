def flatten(xs):
    flattened = []
    for x in xs:
        if isinstance(x, list):
            flattened += flatten(x)
        else:
            flattened.append(x)
    return flattened