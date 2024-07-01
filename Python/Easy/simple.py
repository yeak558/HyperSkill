def round_up(num):
    if num % 1 <= 0.5 and num % 1 != 0:
        num = round(num + 0.5)
        return num
    else:
        return round(num)

print("Enter the loan principal: ", end="\n> ")
principal = int(input())
print("""
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""", end="\n> ")
option = input()
if option == "m":
    print("\nEnter the monthly payment:", end="\n> ")
    pay = int(input())
    m  = round_up(principal / pay)
    print("It will take", m, "months to repay the loan")

elif option == "p":
    print("\nEnter the number of months:", end="\n> ")
    month = int(input())
    p = round_up(principal / month)
    if principal / month != principal // month:
        print(f"\nYour monthly payment = {p} and the last payment = {principal % p}.")
    else:
        print("\nYour monthly payment =", p)

