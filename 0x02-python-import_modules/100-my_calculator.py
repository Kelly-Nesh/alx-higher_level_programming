#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {} <a> <operator> <b>\n{}".format(argv[0], argc))
        exit(1)
    a = int(argv[1])
    op = argv[2]
    ops = ['+', '-', '*', '/']
    b = int(argv[3])
    if op == '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif op == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == '/':
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    else:
        print("Unkown operator. Available operators: {}, {}, {} and {}"
              .format(ops[0], ops[1], ops[2], ops[3]))
        exit(1)
