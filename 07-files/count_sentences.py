
data_file = open("data.txt", "r")

lines = data_file.readlines()

counter = 0

for line in lines:
    sentences = line.split(".")
    for sentence in sentences:
        if sentence != '' and sentence != '\n':
            counter += 1

print("sentences:", counter)