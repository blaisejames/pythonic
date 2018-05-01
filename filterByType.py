sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

varlist = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]

for var in varlist:
    print(var, type(var))
    if isinstance(var, int):
        if var >= 100:
            print("That's a big number\n")
        else:
            print("That's a small number\n")
    elif isinstance(var, str):
        if len(var) >= 50:
            print("Long sentence\n")
        else:
            print("Short sentence\n")
    elif isinstance(var, list):
        if len(var) >= 10:
            print("Big list\n")
        else:
            print("Short list\n")
