peopleNumber = int(input("Enter the number of friends joining (including you):\n> "))

if peopleNumber <= 0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
customers = {}
for i in range(peopleNumber):
    customers[input("> ")] = 0

print("\n", customers)
