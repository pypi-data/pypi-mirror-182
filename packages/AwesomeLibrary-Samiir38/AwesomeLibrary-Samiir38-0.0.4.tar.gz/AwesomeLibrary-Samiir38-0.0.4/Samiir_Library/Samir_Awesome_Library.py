from robot.api.deco import keyword


@keyword
def sum_numbers(a, b):
    print("Sum result is : ", (int(a) + int(b)))


@keyword
def subtract_numbers(a, b):
    print("Subtract result is : ", (int(a) - int(b)))


@keyword
def multiply_numbers(a, b):
    print("Multiply result is : ", (int(a) * int(b)))
