# Strings#1
# string1=input("Mata in en sträng nr 1: ")
# string2=input("Mata in en sträng nr 2: ")
# string3=input("Mata in en sträng nr 3: ")

# stringhopslagen=(f"{string1} {string2} {string3}")
# print(stringhopslagen)

# Strings#2
# sträng="Hello, world"
# index=sträng.find("w")
# print(index)

# Strings#3 Fungerar inte!
# Fungerar inte!
# namn="kurt andersson"
# first=True
# beforeWasSpace=False
# nynamn=""
# for x in namn:
#     if first or beforeWasSpace:
#         nynamn=x.upper()
#     else:
#         nynamn=nynamn+x
#     first=False
#     beforeWasSpace=x==""
# print(nynamn)

# Strings#4
# nr=0
# sträng=("Detta är en sträng som du ska ändra")
# for x in sträng:
#     if x==" ":
#         nr=nr+1
#         x="*"
#     else:continue
# print(f"Det finns {nr} * i strängen")

# Strings#5
# mailadress=input("Skriv in din mailadress: ")
# längd=len(mailadress)
# indexAlfa=mailadress.find("@")
# indexPunkt=mailadress.find(".")
# print(f"längden = {längd}")
# print(f"@= {indexAlfa}")
# print(f".= {indexPunkt}")
# if indexAlfa>0 and indexPunkt>0 and(indexPunkt+4>=längd>=indexPunkt+3):
#     print("Du har matat in en korrekt maildress.")
# else:
#     print("Felaktig mailadress")
    
# Strings#6
# sträng=input("Skriv in en mening: ")
# antalMellanslag=0
# for x in sträng:
#     if x==" ":
#         antalMellanslag=antalMellanslag+1
#     else:continue
# print(f"Antal ord i meningen är {antalMellanslag+1}")

# Strings#7
sträng=input("Skriv in ett ord som kanske är ett palindrom: ")
strängReversed=sträng[::-1]
print(sträng)
print(strängReversed)
if sträng==strängReversed:
    print("Det är ett palindrom")
else:
    print("Det är inte ett palindrom")

# Strings#8 ersätta text med annan.
# while True:
#     txt = input("Skriv text>:")
#     index = txt.find("moron") 
#     if index >= 0:
#         print("Utvisning. Gå och tvätta munnen")
#         break
#     txt = txt.replace("idiot", "*****")
#     txt = txt.replace("dumskalle", "*********")
#     print(txt)







