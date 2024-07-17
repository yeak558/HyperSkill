def round_up(num):
    if num % 1 <= 0.5 and num % 1 != 0:
        num = round(num + 0.5)
        return num
    else:
        return round(num)

import argparse

parser = argparse.ArgumentParser(description="This program prints something")

# Arguments
parser.add_argument("--type_")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

type_ = args.type_
A = float(args.payment) if args.payment != None else args.payment
P = float(args.principal) if args.principal != None else args.principal
n = int(args.periods) if args.periods != None else args.periods
i = float(args.interest) / (100*12) if args.interest != None else None


if A != None and A < 0:
    print("Incorrect parameters")
    exit()
elif P != None and P < 0:
    print("Incorrect parameters")
    exit()
elif n != None and n < 0:
    print("Incorrect parameters")
    exit()
elif i == None:
    print("Incorrect parameters")
    exit()

# Annuity
if type_ == "annuity":
    if all([A, P, i]):
        from math import log
        n = log(A/(A - i * P) , 1+i)
        n = round_up(n)
        if n % 12 == 0:
            print(f"It will take {n//12} years to repay this loan!")
        elif n // 12 == 0:
            print(f"It will take {n%12} months to repay this loan!")
        else:
            print(f"It will take {n//12} years and {n%12} months to repay this loan!")
        print(f"Overpayment = {round_up(n*A-P)}")
    elif all([P, n, i]):
        A = P * ((i * (1+i)**n) / ((1+i)**n -1))
        A = round_up(A)
        print(f"Your annuity payment = {A}!")
        print(f"Overpayment = {round_up(n*A-P)}")
    elif all([A, n, i]):
        P = A / ((i * (1+i)**n)/((1+i)**n - 1))
        print(f"Your loan principal = {int(P)}!")
        print(f"Overpayment = {round_up(n*A-P)}")
    else:
        print("Incorrect parameters")
        exit()

# Differentiated
elif type_ == "diff":
    if all([P, n, i]):
        total = 0
        for m in range(1,n+1):
            Dm = round_up(P/n + i * (P - (P * (m-1))/n))
            total = total + Dm
            print(f"Month {m}: payment is {Dm}")
        overPayment = round_up(total - P)
        print("Overpayment =", overPayment)
    else:
        print("Incorrect Parameters")
        exit()
else:
    print("Incorrect Parameters")
    exit()
