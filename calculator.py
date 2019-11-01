num1 = int(input("Enter number 1: "))

oper = input("Enter the operator: ")

num2 = int(input("Enter number 2: "))

if oper == "*":
    ans = num1 * num2
    print(num1, oper, num2,"=", ans)
elif oper == "/":
    ans = num1 / num2
    print(num1, oper, num2,"=", ans)
elif oper == "+":
    ans = num1 + num2
    print(num1, oper, num2,"=", ans)
elif oper == "-":
    ans = num1 - num2
    print(num1, oper, num2,"=", ans)
