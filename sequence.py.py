n = int(input("Enter the length of the sequence: "))
count_num = 3
num1 = 1
num2 = 2
num3 = 3
for i in range(1, n+1):
    if 1 <= i <=3:
        print(i)
    else:
        total = num1 + num2 + num3
        num1= num2
        num2= num3
        num3= total
        print(total)
    
