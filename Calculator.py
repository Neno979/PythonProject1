again = "y"
while again == "y":
#collecting first float number
    while True:
        try:
            a = float(input("Please enter first number:"))
            break
        except ValueError:
            print("this is not a number!")
#collecting second float number
    while True:
        try:
            b = float(input("Please enter second number:"))
            break
        except ValueError:
            print("this is not a number!")
#colecting arithmetic operation and writing result
    while True:
        operand = input("Please enter one of the following arithmetic operation +,-,/,*:")
        if operand == "+":
            print("a + b =",a+b)
            break
        elif operand == "-":
            print("a - b =",a-b)
            break
        elif operand == "*":
            print("a * b =",a*b)
            break
        elif operand == "/":
            print("a / b =",a/b)
            break
        else:
            print("operation is not valid!")
#looping the process of calculation
    again = input("if you want to continue enter y else press enter:")
