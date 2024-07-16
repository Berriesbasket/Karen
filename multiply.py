# author: karen chan
# github username: berriesbasket
# date: 7-17-24
# description: takes two positive integers as parameters and returns the product of those two numbers.

def multiply(num_1, num_2):
    """returns the product of two numbers."""
    if num_1 == 1:
        return num_2
    if num_2 == 1:
        return num_1

    return num_1 + multiply(num_1 , num_2 - 1)



print(multiply(5, 7))