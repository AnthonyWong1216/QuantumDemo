#This is a comment

myName = "Mark"

myPhone = "1234567890"

print(myName, myPhone)

changingType = 1
changingType = "I am now a string"
print(changingType)

one, two = 1, 2

print(one, two)

myName, myPhone = myPhone, myName

print(myName, myPhone)

def retTwo():
    return 3, 4

three, four = retTwo()

print(three, four)

print(__name__) # The value of __name__ is "__main__" if called directly, 
                # or the name of the module if imported as a module