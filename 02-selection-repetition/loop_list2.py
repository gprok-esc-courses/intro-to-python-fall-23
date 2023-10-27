s = "No man crosses the same river twice."

ch = input("Give a character: ")

counter = 0
for character in s.lower():
    if character == ch:
        counter = counter + 1

print(counter)