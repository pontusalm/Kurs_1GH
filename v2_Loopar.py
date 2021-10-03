# # Loop#1
# for tal in range(0,11):
#     print (tal)

# tal=0
# while tal<11:
#     print (tal)
#     tal=tal+1

# Loop#2
# tal1=int(input("Skriv in tal 1: "))
# tal2=int(input("Skriv in tal2: "))
# # for tal in range(tal1+1,tal2):
# #     print (tal)

# tal=tal1+1
# while tal<tal2:
#     print (tal)
#     tal=tal+1

# Loop#3
# while True:
#     tal1=int(input("Ange tal1: "))
#     tal2=int(input("Ange tal2: "))
#     summa=tal1+tal2
#     print(f"summan är {summa}")
#     sel=input("Vill du fortsätta? J/N ")
#     if sel==("N"):
#         print("Vi slutar")
#         break
#     else:
#         continue

# Loop#4
# iteration=0
# talSumma=0
# while iteration<10:
#     tal=int(input("Mata in ett tal: "))
#     talSumma=talSumma+tal
#     iteration=iteration+1
# print (f"Summan av dina tal är {talSumma}")

# # Loop#5
# tal=int(input("Mata in ett tal: "))
# while tal>0:
#     print(tal)
#     tal=tal-1

# Loop#6
import random
dice1=0
while True:
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print("rolling the dices")
    print (f"The values are...\n{dice1} and {dice2}")
    sel=input("Roll the dices again y/n ?: ")
    if sel=="n":
        break
    else:continue

