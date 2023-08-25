#!/usr/bin/python3
msg = "hello, world!"
print(msg)
print(msg.title())
print(msg.upper())
print(msg.lower())
print("Hello" + ", World!") #string concatenation
name = "Alex"
print(f"Hello {name}")
names = ['John', 'Mike']
print(names)
names.append('James')
print(names)
names.insert(0, 'Daniel')
print(names)
del names[0]
print(f"names = {names}")
names.remove('John')
print(f"names = {names}")

