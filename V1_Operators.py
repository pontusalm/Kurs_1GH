name=("Pontus")
age= int (59)
print ("Jag heter", name,"och är", age, "år.")
print (f"Jag heter {name} och är {age} år.")


Fornamn=input("Mata in ditt förnamn: ")
Efternamn=input("Mata in ditt efternamn: ")
print(f"Du heter: {Efternamn}, {Fornamn}")


Tal1=int (input("Mata in tal 1:"))
Tal2=int (input("Mata in tal 2:"))

Tal3=Tal1**Tal2
print(f"Tal1 upphöjt till Tal2 = {Tal3}")
Tal3=Tal1*Tal2
print(f"Tal1 gånger Tal2 = {Tal3}")
Tal3=Tal1/Tal2
print(f"Tal1 delat med Tal2 = {Tal3}")
Tal3=Tal1//Tal2
print(f"Tal1 heltalsdividerat med Tal2 = {Tal3}")
Tal3=Tal1%Tal2
print(f"Resten från heltalsdivision av Tal1 med Tal2 = {Tal3}")

Namn=input("Mata in ditt namn")
i=1
while i<6:
    print(Namn)
    i=i+1

Resultat = False
Tal=int(input("Mata in ett tal"))
print(Tal>100)
