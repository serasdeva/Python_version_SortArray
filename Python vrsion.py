listA = ["hello", "2", "world", ":-)"]
listB = []
for i in listA:
    if len(i) <= 3:
        listB.append(i)

print(listB)