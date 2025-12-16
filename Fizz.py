imp = int(input("Please enter a number between 1 and 100:"))
for i in range(imp,100):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
