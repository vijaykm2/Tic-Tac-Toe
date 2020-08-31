inpt = ""
guests = []
while inpt != ".":
    inpt = input()
    if inpt != ".":
        guests.append(inpt)

print(guests)
print(len(guests))