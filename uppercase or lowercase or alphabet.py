#write a python program to check weather a character is uppercase or lowercase alphabet.
ch=input("enter character")
if ch<="a" and ch>="z":
    print("lowercase")
elif ch<="A" and ch>="Z":
    print("uppercase")
else:
    print("not alphabet")
