peopleNumber = int(input("Enter the number of friends joining (including you):\n> "))

if peopleNumber <= 0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
customers = {}
for i in range(peopleNumber):
    customers[input("> ")] = 0

bill = int(input("Enter the total bill value:\n> "))

if bill/peopleNumber == int(bill/peopleNumber):
    for key in customers:
        customers[key] = int(bill/peopleNumber)
else:
    for key in customers:
        customers[key] = round(bill/peopleNumber,2)

print("\n", customers)
