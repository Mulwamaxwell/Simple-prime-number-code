number = int(input("number:"))
if number == 1:
    print("The number is not a prime number ")
elif number > 1:
    for x in range(2, number):
        if (number % x) == 0:
            print("Number is not prime")

            break
    else:
        print(number, "is a prime number")
