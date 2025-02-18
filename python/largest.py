print("Enter Number of elements you want to enter")
count = int(input())
print("Enter the elements")
arr=[]
for i in range(0,count):
    arr.append(int(input()))
max = 0

for i in range(0,count):
    if arr[i]>max:
        max = arr[i]

print("Largest element is: ",max)
