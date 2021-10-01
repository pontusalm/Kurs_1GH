Tal=int(input("Mata in ett tal: "))
if Tal>10:
    print("Talet är större än 10")
else:
    print("Talet är mindre än 10")

# IF#2
AntalPpaketKvar=int(input("Mata in hur många paket mjölk som finns kvar: "))
if AntalPpaketKvar<10:
    print("Beställ 30 paket")
elif AntalPpaketKvar<20:
    print("Beställ 20 paket")
else:
    print("Du behöver inte beställa någon mjölk")

# IF#3
Number1=int(input("Mata in tal nr 1: "))
Number2=int(input("Mata in tal nr 2: "))
if Number1>Number2:
    largest=Number1
else:
    largest=Number2
print(f"Det största talet är {largest}")

# IF#4
Number1=int(input("Mata in tal nr 1: "))
Number2=int(input("Mata in tal nr 2: "))
Number3=int(input("Mata in tal nr 3: "))
if Number1>Number2 and Number1>Number3:
    largest=Number1
elif Number2>Number1 and Number2>Number3:
    largest=Number2
else:
    largest=Number3
print(f"Det största talet är {largest}")

# IF#5
kategori=input("Mata in vilken kategori du tillhör: vuxen, pensionär eller student: ")
if kategori=="pensionär" or kategori=="student":
    print("Din resa kostar 20kr ")
elif kategori=="vuxen":
    print("Din resa kostar 30 kr")
else:
    print("Du har angett en felaktig kategori")

# IF#6
födelseår=int(input("Mata in ditt födelseår: "))
if födelseår>=1980 and födelseår<1990:
    print("Du är född på 1980-talet ")
elif födelseår>=1990 and födelseår<2000:
    print("Du är född på 1990-talet ")
else:
    print("Du är inte född på 1990- eller 1980-talet")

# IF#7
land=input("Mata in vilket land du bor i: ")
if land=="Sverige" or land=="Norge" or land=="Danmark":
    print("Du bor i Skandinavien")
else:
    print("Du bor inte i Skandinavien")

# IF#8
summa=int(input("Hur mycket pengar har du? "))
rabatt=input("Har du rabatt? ")
if 15<summa<25 and rabatt=="nej":
    print("Du kan köpa en liten hamburgare")
elif 15<summa<25 and rabatt=="ja":
    print("Du kan köpa en liten hamburgare och pommes frites")
elif 25<summa<=50 and rabatt=="nej":
    print("Du kan köpa en stor hamburgare och pommes frites")
elif 25<summa<=50 and rabatt=="ja":
    print("Du kan köpa en stor hamburgare med pommes frites")
elif 50<summa<=60 and rabatt=="ja":
    print("Du kan köpa ett meal med dryck")
elif summa>60:
    print("Du kan köpa ett meal med dryck")
else:
    print("Du kan tyvärr inte köpa något")




