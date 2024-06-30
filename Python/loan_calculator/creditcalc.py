def round_up(num):
    if num % 1 < 0.5 and num % 1 != 0:
        num = round(num + 0.5)
        return num
    else:
        return round(num)

import argparse

parser = argparse.ArgumentParser(description="This program prints something")

# Arguments
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

A = float(args.payment) if args.payment != None else args.payment
P = float(args.principal) if args.principal != None else args.principal
n = int(args.periods) if args.periods != None else args.periods
i = float(args.interest) / (100*12)


if all([A, P, i]):
    from math import log
    n = log(A/(A - i * P) , 1+i)
    n = round_up(n)
    print(f"> It will take {n//12} years and {n%12} months to repay this loan!")
elif all([P, n, i]):
    A = P * ((i * (1+i)**n) / ((1+i)**n -1))
    A = round_up(A)
    print(f"> Your monthly payment = {A}!")
elif all([A, n, i]):
    P = A / ((i * (1+i)**n)/((1+i)**n - 1))
    print(f"> Your loan principal = {int(P)}!")



