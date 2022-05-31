#Accept any city from the user and display the monument of that city.
 #      city                Monument
 #      Delhi                Red fort
 #      Agra                 Taj mahal
 #      Jaipur               Jal mahal
city=input("enter any city")
if city=="Delhi":
    print("Red fort")
elif city=="Agra":
    print("Taj Mahal")
elif city=="Jaipur":
    print("Jal mahal")
else:
    print("none")