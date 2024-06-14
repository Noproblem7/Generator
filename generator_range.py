def generator_range(birinchi, ikkinchi=None, uchinchi=None):
    if ikkinchi is None:
        start = 0
        stop = birinchi
        step = 1
    elif uchinchi is None:
        start = birinchi
        stop = ikkinchi
        step = 1
    else:
        if uchinchi == 0:
            raise ValueError()
        start = birinchi
        stop = ikkinchi
        step = uchinchi

    i = start
    if step > 0:
        while i < stop:
            yield i
            i += step
        return i
    elif step < 0:
        while i > stop:
            yield i
            i += step
        return i


for i in generator_range(4, 12, 0.5):
    print(i)
