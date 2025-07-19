#!/usr/bin/env python3
import argparse

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def main():
    parser = argparse.ArgumentParser(description="Simple CLI calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add two numbers")
    parser_add.add_argument("x", type=float)
    parser_add.add_argument("y", type=float)

    parser_sub = subparsers.add_parser("sub", help="Subtract two numbers")
    parser_sub.add_argument("x", type=float)
    parser_sub.add_argument("y", type=float)

    parser_mul = subparsers.add_parser("mul", help="Multiply two numbers")
    parser_mul.add_argument("x", type=float)
    parser_mul.add_argument("y", type=float)

    parser_div = subparsers.add_parser("div", help="Divide two numbers")
    parser_div.add_argument("x", type=float)
    parser_div.add_argument("y", type=float)

    args = parser.parse_args()

    if args.command == "add":
        result = add(args.x, args.y)
    elif args.command == "sub":
        result = sub(args.x, args.y)
    elif args.command == "mul":
        result = mul(args.x, args.y)
    elif args.command == "div":
        result = div(args.x, args.y)

    print(result)

if __name__ == "__main__":
    main()
