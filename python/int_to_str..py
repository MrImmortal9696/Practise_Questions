s="0123456789"
num=int(input("Enter the number"))
result = ""
if num == 0:
    print("0")
else:
    while(num > 0):
        result =  result+s[num%10]
        num= num//10
    print(type(result))
    print(result)
