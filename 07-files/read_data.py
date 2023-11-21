
try:
    data_file = open("data.txt", "r")

    lines = data_file.readlines()

    for line in lines:
        print(line)
        
except FileNotFoundError:
    print("File not found")

