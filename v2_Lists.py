# Lists#1
# tallista=[]
# i=1
# largest=0
# while i<5:
#     tal=int(input("Mata in ett tal: "))
#     tallista.append(tal)
#     i=i+1

# for tal in tallista:
#     if tal>largest:
#         largest=tal
# print(f"Det största talet är {largest}")

# Lists#2
# tallista=[2,3,67,89,25]
# summa=0
# for siffra in tallista:
#     summa=summa+siffra
# print(f"Summan av talen är {summa}")

# Lists#3
# tallista=[2,56,7,89,3456,456,789]
# largest=0
# for tal in tallista:
#     if tal>largest:
#         largest=tal
# print(f"Det största talet är {largest}")

# Lists#4
# stränglista=["abc","xyz","aba","1221","hammarbyh"]
# antal=0
# for sträng in stränglista:
#     if len(sträng)>=2 and (sträng[0]==sträng[-1]):
#         antal=antal+1
# print(antal)

# Lists#5
# stränglista=["abc","xyz","abc","1221","hammarbyh"]
# stränglistaNoDup=set(stränglista)
# print(stränglistaNoDup)

# #Alternativ lösning.
# talLista = [12,34,566,1,56,5,1,34,55]
# talListaNy = []
# for x in talLista:
#     if not x in talListaNy:
#         talListaNy.append(x)
# print(talListaNy)

# Lists#6
# stränglista=["abc","xy","abc","1221","hammarbyh","Oslo","Göteborg"]
# stränglistaNy=[]
# ordlängd=int(input("Hur långa ord vill du ta fram? "))
# for sträng in stränglista:
#     if len(sträng)>=ordlängd:
#         stränglistaNy.append(sträng)
#     else:continue
# print(stränglistaNy)

# Lists#6


