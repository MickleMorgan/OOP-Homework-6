def geometric_gen(start, q):
    while True:
        yield start
        start *= q


sequence = geometric_gen(2, 9)
for item in sequence:
    if item > 10_000:
        sequence.close()
        break

    # print(item)


def new_range(*args):
    if len(args) == 1:
        stop = args
    if len(args) == 2:
        start, stop = args
    if len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError

    if not (isinstance(start, int) and isinstance(stop, int) and isinstance(step, int)):
        raise ValueError
    if not step or (step < 0 and stop > start) or (step > 0 and stop < start):
        return

    while abs(start) < abs(stop):
        yield start
        start += step


# print(*new_range(1, -10, -2))

def prime_gen(stop):
    for i in range(stop + 1):
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            yield i


# for i in prime_gen(1000):
#     print(i)

def list_filler(stop):
    start = 2
    while start <= stop:
        yield start ** 3
        start += 1


list1 = [item for item in list_filler(20)]
print(list1)