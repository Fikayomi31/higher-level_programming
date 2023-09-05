#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, opr, b = args
    if opr not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(a)
    b = int(b)
    
    if opr == '+':
        print("{} {} {} = {}".format(a, opr, b, add(a, b)))
    elif opr == '-':
        print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
    elif opr == '*':
        print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
    elif opr == '/':
        print("{} {} {} = {}".format(a, opr, b, div(a, b)))
