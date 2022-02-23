# homework 1.3: Calculator

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
op=input("Choose an arithmetic operation: ")
print()

if op == "+":
    print("The result is:",a+b)
elif op == "-":
    print("The result is:",a-b)
elif op == "*":
    print ("The result is:",a*b)
elif op == "/":
    if b!=0:
        print("The result is:",a/b)
    else:
        print("Error! Division by zero not defined!")
else:
    print("You haven't entered an arithmetic operation!")
