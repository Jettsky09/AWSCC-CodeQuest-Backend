Times = int(input("Times: "))
i=1
while (i <= Times):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
