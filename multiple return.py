a = 32
b = 20

# addition = a + b
# subs = a - b
# print(addition, subs)

def add_sub(a,b):
    """
    this will return addition and substruction of two number
    :param a: first number
    :param b:  second number
    :return: addtion and substruction
    """
    addition = a + b
    subs = a - b
    return addition, subs


# print(add_sub.__doc__)
# print(add_sub(40, 25))

result = add_sub(40, 25)
print(type(result))