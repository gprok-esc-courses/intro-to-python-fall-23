
out_file = open("out.txt", "w")

while True:
    txt = input("type a name ('exit' to close): ")
    if txt == 'exit':
        break
    out_file.write(txt + "\n")

out_file.close()