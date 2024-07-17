earned_amount = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250, 'Milk chocolate': 1680, 'Doughnut': 1075, 'Pancake': 80}

income = 0
print("Earned amount:")
for key, value in earned_amount.items():
    print(key,": $",value,sep="")
    income = income + value

print(f"Income: ${float(income)}")
print("Staff expenses:\n>",end="")
staff = int(input())
print("Other expenses:\n>",end="")
other = int(input())
income = income - staff - other
print(f"Net income: ${float(income)}")
