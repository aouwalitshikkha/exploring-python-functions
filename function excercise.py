# Write a Python function to multiply all the numbers in a list.

# Write a Python function that takes a number as a parameter and
# check the number is prime or not.

numbers = [2, 6, 9, 8, 8, 15, 1, 5, 88]


def multiply_list(list):
    result = 1
    for number in list:
        result *= number
    return result

result = multiply_list(numbers)
# print(result)

def check_prime(number):
    if (number == 1):
        return False
    elif(number == 2):
        return True
    else:
        for x in range(2,number):
            if (number % x) == 0:
                return False
            else:
                return True

print(check_prime(75))

