for i in range(1,10):
    n = int(input("Enter Number"))
    if n == 18:
        print("Your guesses is correct")
        break
    elif n>18:
        print("Enter smaller number","Number of guesses left",(9-i))
        continue
    elif n<18:
        print("Enter larger number","Number of guesses left",(9-i))
        continue
else:
    print("Game over")
print("No of guesses took to finish is",i)
