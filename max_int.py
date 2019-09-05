num_int = 0
total = 0
max_int = 0

while True:
    num_str = input("Input a number: ")
    num_int = int(num_str)
    if num_int < 0:
        if total >= 0:
            print("The maximum is", max_int)
        break
    total += 1

    if max_int is 1:
        max_int = num_int
    elif max_int < num_int:
        max_int = num_int


