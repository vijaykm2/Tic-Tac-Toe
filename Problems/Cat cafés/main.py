inpt = ""
catCafes = []
while inpt != "MEOW":
    inpt = input()
    if inpt != "MEOW":
        catCafes.append(inpt)


largest = ''
largestNum = -1
for cafe in catCafes:
    cafeNum = int(cafe.split()[1])
    if(cafeNum > largestNum):
        largest = cafe.split()[0]
        largestNum = cafeNum

print(largest)
