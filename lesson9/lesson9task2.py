def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)
