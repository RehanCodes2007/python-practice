nums = (19, 22, 33, 40, 50, 60, 33, 90, 70, 33)
x = int(input("Enter a Number:"))
i = 0
while i < len(nums):
    if(nums [i] == x):
        print("FOUND at idx:", i)
        break
    else:
        print("Finding.....")
    i += 1
print("end of loop")

