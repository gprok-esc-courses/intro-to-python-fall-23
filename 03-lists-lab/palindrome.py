n = int(input("give a number: "))

digits = []

if n < 0:
    print("Not a palindrome")
else: 
    temp = n
    while temp != 0:
        r = temp % 10
        digits.append(r)
        temp = temp // 10

    print(digits)

    reverse_digits = digits[::-1]

    print(reverse_digits)

    is_palindrome = True
    for i in range(len(digits)):
        if digits[i] != reverse_digits[i]:
            is_palindrome = False
            break

    if is_palindrome:
        print("It is a palindrome")
    else:
        print("Not a palindrome")
