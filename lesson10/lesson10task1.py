def some_gen(begin, n, func):
    value = begin
    for _ in range(n):
        yield value
        value = func(value)
