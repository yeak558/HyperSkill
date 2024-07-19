bot_name = "Bot"
print(f"Hello! My name is {bot_name}.")
print("I was created in 2024.")
print("Please, remind me your name.\n> ",end="")
user_name = input()
print(f"What a great name you have, {user_name}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
stop = int(input("> "))

for i in range(stop+1):
    print(i,"!")

print("""
Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")
answer = input("> ")
while answer != "2":
    print("Please, try again.")
    answer = input("> ")

print("Completed, have a nice day!")

