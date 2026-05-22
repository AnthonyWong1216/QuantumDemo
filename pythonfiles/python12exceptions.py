#Exception Handling

try:
    print(1/0)
except Exception as whatWentWrong:  
    print(whatWentWrong)
#Instead of a catch-all you should use specific exception types!