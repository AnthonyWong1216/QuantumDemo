#Lists (Equivalent of Arrays)

emptyList = []

mixedTypes = [1, 2, "Hello"]

listOfLists = [[1,2,3],[4,5,6],[7,8,9]]

print(len(listOfLists))

emptyList.append("first")
emptyList.append("second")
print(emptyList)

del emptyList[0]
print(emptyList)

print(mixedTypes.index("Hello"))


#Tuples - Lists that are immutable

myTuple = (1, 2, "Bye")
print(myTuple[2])