#Loops

n = 0
while n<10:
    print(n)
    n+=1 #There is no ++ operator!
    
myFriends = ["John", "Jack", "Alice", "Bob"]

for friend in myFriends:
    print(friend)
    
for friend in myFriends:
    if(friend == "Jack"):
        continue
    if(friend == "Alice"):
        break
    print(friend)
    
for i in range(5,10): #same as for(i=5;i<10;i++) in other languages
    print(i)
    
doubleFriends = [friend+friend for friend in myFriends]
print(doubleFriends)

squares = [num*num for num in range(0,5)]
print(squares)