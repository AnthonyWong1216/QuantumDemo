#Dictionary - Name-value pairs / associative array / map / lookup table

myDict = {}

myDict["first"] = "This is the first value"
myDict["second"] = "This is value 2"

print(myDict["first"])

literalDictionary = {"key1":"value1", "key2":"value2"}
print(literalDictionary["key2"])

del literalDictionary["key1"]

print(len(literalDictionary))

print("key1" in literalDictionary)
print("key2" in literalDictionary)