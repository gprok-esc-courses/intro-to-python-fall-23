
data_file = open("data.txt", "r")

lines = data_file.readlines()

counter = 0

for line in lines:
    sentences = line.split(".")
    for sentence in sentences:
        if sentence != '' and sentence != '\n':
            words = sentence.split(" ")
            counter += len(words)

print("words:", counter)