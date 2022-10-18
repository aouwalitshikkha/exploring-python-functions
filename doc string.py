# Write a python function to convert fahrenheit to celsius
# c = 5/9 * (f-32)

def fahrenheit_celsius(fahrenheit):
    """
    This function will convert fahrenheit to celcious
    :param fahrenheit: it takes fahrenheit temparature as parameters
    :return: It will return celsius temperature
    """
    celsius = 5 / 9 * (fahrenheit-32)
    return celsius

# print(fahrenheit_celsius(100))
name = 'Abdul Aouwal'
print(fahrenheit_celsius.__doc__)
