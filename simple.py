# print('Hello, world!')

# num1 = int(input('Enter first number: ', ))
# print(num1)

# if num1 % 2:

#     print("Odd")


# else:
#     print("Even")

# a = 2
# b = 3

# while a <= 5:

#     print(a)
#     a += 1


print("Calculator App Py")


num1 = int(input("Press 1 To Continue Or Any Other Key To Exit\n"))

if num1 == 1:
    sign = input("Press + for Addition\n"
                 "Press - for Subtraction\n"
                 "Press * for Multiplication\n"
                 "Press / for Division\n "
                 )

    if sign == '+':
        n1 = int(input("Enter First Number\n"))
        n2 = int(input("Enter Second Number\n"))
        res = n1 + n2
        print(n1, sign, n2, '=', res)

    elif sign == '-':
        n1 = int(input("Enter First Number\n"))
        n2 = int(input("Enter Second Number\n"))
        res = n1 - n2
        print(n1, sign, n2, '=', res)

    elif sign == '*':
        n1 = int(input("Enter First Number\n"))
        n2 = int(input("Enter Second Number\n"))
        res = n1 * n2
        print(n1, sign, n2, '=', res)

    elif sign == '/':
        n1 = int(input("Enter First Number\n"))
        n2 = int(input("Enter Second Number\n"))
        res = n1 / n2
        print(n1, sign, n2, '=', res)

    elif sign:
        print("Incorrect Input ")
        exit()


else:
    exit()
