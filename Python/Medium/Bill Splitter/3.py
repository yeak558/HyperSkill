peopleNumber = int(input("Enter the number of friends joining (including you):\n> "))

if peopleNumber <= 0:
    print("No one is joining for the party")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
customers = {}
for i in range(peopleNumber):
    customers[input("> ")] = 0

bill = int(input("Enter the total bill value:\n> "))

choice = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')
if choice == "Yes":
    from random import choice
    names = []
    for i in customers:
        names.append(i)

    lucky = choice(names)
    print("\n" + lucky + " is the lucky one!")
else:
    print("No one is going to be lucky")


