print("Hey! I am a calculator. Would love to help you :)")
print("Here's what I can do for you:")
print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Finding a square ")
exit = 6
choice = 0
while choice != exit:
    choice = int(input("Enter your choice (type 6 if you want to exit):"))
    if choice==1:
        numbers = int(input("How many numbers you want to add?(I can add max 3 numbers)"))
        if numbers == 2:
           x = int(input("Enter first number: "))
           y = int(input("Enter second number: "))
           print("The result is",x+y)
        elif numbers == 3:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            z = int(input("Enter third number: "))
            print("The result is",x+y+z)
        else:
            print("Sorry! I can do maximum 3 numbers addition:(")
    elif choice == 2:
        numbers = int(input("How many numbers you want to subtract?(I can subtract max 3 numbers)"))
        if numbers == 2:
           x = int(input("Enter first number: "))
           y = int(input("Enter second number: "))
           print("The result is",x-y)
        elif numbers == 3:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            z = int(input("Enter third number: "))
            print("The result is",x-y-z)
        else:
            print("Sorry! I can do maximum 3 numbers subtraction:(")
    elif choice == 3:
        numbers = int(input("How many numbers you want to multiply?(I can multiply max 3 numbers)"))
        if numbers == 2:
           x = int(input("Enter first number: "))
           y = int(input("Enter second number: "))
           print("The result is",x*y)
        elif numbers == 3:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))
            z = int(input("Enter third number: "))
            print("The result is",x*y*z)
        else:
            print("Sorry! I can do maximum 3 numbers multiplication:(")
    elif choice == 4:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        if y==0:
            print("In Maths, we can't divide by 0:(")
        else:
            print("The result is",x/y)
    elif choice == 5:
        x = int(input("Enter the number you want square of: "))
        print("The result is", x ** 2)
    elif choice>6 or choice<1 :
        print("Invalid choice:(")
if choice == 6:
    print("It was nice to meet you. Goodbye:)")

        