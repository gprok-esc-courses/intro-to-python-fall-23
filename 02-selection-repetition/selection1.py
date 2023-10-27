age = int(input("Give your age: "))
job = input("Job?: ")

if age < 18:
    print("Not allowed")
    print("Do not enter")
else:
    print("OK to watch")

if age < 18:
    print("No need for vaccination")
elif age < 60:
    print("Do the basic vaccine")
else:
    print("Do the advanced vaccine")

if age < 18:
    print("Basic course")
else:
    if job == "Programmer":
        print("Advanced course")
    else:
        print("Basic course")