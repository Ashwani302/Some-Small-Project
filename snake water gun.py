import random
print("Snake\nWater\nGun")
a =0
b =0
c =0
for i in range(10):
    n = ["Snake","Water","Gun"]
    m = random.choice(n)
    q = str(input("Enter Your Choice: "))
    if m == "Snake" and q == "Water":
        print("You Win",10-i)
        a +=1
    elif m == "Snake" and q == "water":
        print("You Win",10-i)
        a +=1
    elif m =="Snake" and q == "Gun":
        print("You Win",10-i)
        a += 1
    elif m =="Snake" and q == "gun":
        print("You Win",10-i)
        a += 1
    elif m =="Snake" and q == "Snake":
        print("Draw",10-i)
        c +=1
    elif m =="Snake" and q == "snake":
        print("Draw",10-i)
        c +=1
    elif m =="Water" and q =="Water":
        print("Draw",10-i)
        c +=1
    elif m =="Water" and q =="water":
        print("Draw",10-i)
        c +=1
    elif m == "Water" and q == "Gun":
        print("You Loss",10-i)
        b +=1
    elif m == "Water" and q == "gun":
        print("You Loss",10-i)
        b +=1
    elif m == "Water" and q == "Snake":
        print("You Loss",10-i)
        b += 1
    elif m == "Water" and q == "snake":
        print("You Loss",10-i)
        b += 1
    elif m =="Gun" and q =="Gun":
        print("Draw",10-i)
        c +=1
    elif m =="Gun" and q =="gun":
        print("Draw",10-i)
        c +=1
    elif m == "Gun" and q == "Water":
        print("You Loss",10-i)
        b +=1
    elif m == "Gun" and q == "Water":
        print("You Loss",10-i)
        b +=1
    elif m == "Gun" and q == "Snake":
        print("You Loss",10-i)
        b =+ 1
    else:
        print("Invalid Input")
    print(m)
print("You Win",a,"Times")
print("You Loss",b,"Times")
print("Draw",c,"Times")
