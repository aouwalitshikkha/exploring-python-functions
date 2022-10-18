def add(a, b):
    return a + b


def addition(a, b, c):
    return a + b + c


# print(add(3, 4))
# print(addition(3, 4, 5))

def multiple_additin(*number):
    sum = 0
    for n in number:
       sum += n

    return sum


# print(multiple_additin(2, 3, 4,10, 15))
