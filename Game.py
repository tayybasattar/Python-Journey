username = input("Enter username: ")
password = input("Enter password: ")
if username=="admin" and password=="1234":
    message = "Welcome!"
    print(message)
    print("========Secret Game========")
    secret = 8
    tries = 0
    while tries<3:
        x = int(input("Enter a number(1-10): "))
        if x==secret:
            print("Yay! You guessed it correctly")
            break
        else:
            tries+=1
            if tries<2:
                print("Incorrect!")
                if x<secret:
                    print("Too low!")
                else:
                    print("Too High!")
            else:
                tries+=1
                print("Incorrect!")
                if x<secret:
                    print("Too low!")
                else:
                    print("Too High!")
                print("Its your last chance to guess.")
                guess = int(input("Enter your last guess: "))
                if guess==secret:
                    print("Yay! You guessed it correctly")
                else:
                    print(f"You lost your chance:( The secret number was {secret}.")
else:
    print("Invalid credentials.")

    


    

    



