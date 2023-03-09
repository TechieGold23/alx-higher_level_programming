#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import mul, add, sub, div

    a = 10
    b = 5

    addition = add(a, b)
    multiply = mul(a, b)
    subtract = sub(a, b)
    divide = div(a, b)

    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, subtract))
    print("{} * {} = {}".format(a, b, multiply))
    print("{} / {} = {}".format(a, b, divide))
