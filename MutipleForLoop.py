
number = int(input("Enter the number: "))

x = 0

if number == 0:
    for number in range(12):
        if number == 0:
            number = 2
        else:
            number = number + 1
        for x in range(12):
            x = x + 1
            y = number * x
            print(number, " X ", x, " = ", y)
else:
    for x in range(12):
        x = x + 1
        y = number * x
        print(number, " X ", x, " = ", y)
    

#for x in range(12):
#    x = x + 1
#    y = number * x
#    print(number, " X ", x, " = ", y)
