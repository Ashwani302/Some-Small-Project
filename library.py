class library:
    def display(self, name):
        print("Welcome",name, end=" ")

    def lend(self, dict):
        a = input("Enter Which Book You Want: ")
        if a not in books:
            print(a,"Not Available")
        if a in books:
            b = str(input("Enter Your Name: "))
            f = open("dict.txt", "a")
            m = f.write("The Person is" + b + "\n")
            print(f"{a} is now with you {b}")
            return f"{dict.remove(a)}"
        else:
            print(f"This is lended to a client",)


    def add(self, dict):
        a = input("Enter Book Name You want to Add: ")
        print(f"{a} is added to library")
        return f"{dict.append(a)}"

    def ret(self, list):
        a = input("Enter Book Name Want To Return: ")
        b = str(input("Enter Your Name: "))
        print(f"{a} is returned to library by {b}")
        return f"{list.append(a)}"


m = library()
books = ['Available books are- ', 'Rich Dad Poor Dad', "Mushoku Tensie",
         "Harry Potter",
         "Python Crase Course by harry"]
m.display("World Library")
print(books)
while(True):
    print("\nWhat do you want to do\n"
          "1.Display Book\n"
          "2.Lend Book\n"
          "3.Add Book\n"
          "4.Return Book\n"
          "5.Exit")
    choice = 0
    choice = int(input("Enter your choice(1-4): "))
    if choice == 1:
        m.display(books)
    elif choice == 2:
        m.lend(books)
    elif choice == 3:
        m.add(books)
    elif choice == 4:
        m.ret(books)
    elif choice == 5:
        break
    else:
        print("invalid input")
