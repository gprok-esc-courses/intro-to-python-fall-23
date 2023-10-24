s1 = "Hello"
s2 = 'Hello'
s3 = "      Hello!      "

m = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Ut gravida mollis turpis sit amet fringilla. Orci varius natoque 
penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
Nulla tempus tempor fringilla. Sed tristique interdum consectetur. 
Ut at cursus nisi. Pellentesque tempus blandit magna, id semper 
nisl congue et. Phasellus feugiat ultricies mi, et aliquam lectus 
iaculis tincidunt. Sed nec risus non ante tincidunt pretium. 
Nulla a hendrerit nisi, nec faucibus purus. Donec massa ipsum, 
elementum interdum felis non, elementum molestie orci. Ut id 
libero lobortis arcu faucibus semper non sed nunc.'''

# print(m)

# Display a character at a specific position in a string
print(s1[3])
print(m[600:])
print(s2[-2])

print(len(s1))
print(len(m))

print("asd" not in m)

print(s2.upper())
print(s2.lower())
print(s3)
print(s3.strip())

print(s2.replace("H", "G"))

# String concatenation
v = 100
z = 1
a = "Hello " + "World" + "! " + str(v) + " wishes"
print(a)

b = "Hello World! {} and {} wishes"
print(b.format(v, z))

print("Hello \"big\" World!")
print("Hello \\\" \nWorld!")

print(m.count("id"))

d = 7.9
b = True

print(type(v))
print(type(m))
print(type(d))
print(type(b))