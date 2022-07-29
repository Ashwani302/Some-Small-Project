import os


def word(path1, file, format):
    os.chdir(path1)
    a1 = os.listdir(path1)
    i = 1
    # print(os.getcwd())
    with open(file) as f:
        c1 = f.read().split("\n")
    for file in a1:
        if file not in c1:
            os.rename(file, file.capitalize())
        if format == os.path.splitext(file)[1]:
            os.rename(file, f"{i}{format}")
            i += 1


# a = input("Enter Path: ")
# b = input("Enter File: ")
# c = input("Enter Format: ")
word(r"E:\bca", r"C:\Users\ashwa\PycharmProjects\pythonProject1\filereader00.py", ".pdf")
