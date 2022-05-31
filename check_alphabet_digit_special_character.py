#write a python program to input any character and check weather it is alphabet ,digit or special character.
ch=input("enter a character")
if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
    print("it is alphabet")
elif ch>="0" and ch<="9":
    print("it is digit")
else:
    print("special character")