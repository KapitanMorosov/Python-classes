open_file = open(r"C:\Users\Alan\Downloads\hello.txt","r")
search = open_file("read")

for char in search:
    if(char.isupper()):
        uppercase += 1
        