"""
#this is a comment


3 quote
this is a comment


prints a name combined with the string
name = input("What's your name? ")
print("Hello," + name)
output: Hello,des

name = input("What's your name? ")
print("Hello, ", name)
output: Hello,  deqw
#automatically add space

name = input("What's your name? ")
print("Hello, ", end="")
print(name)
output: Hello, sora
#removes and replace the automatic \n from the print function

#ex2:
name = input("What's your name? ")
print("Hello", end=", ")
print(name)
output: Hello, sora

name = input("What's your name? ")
print("Hello", name, sep="???")
output: Hello???exs
#overrides the automatic space in between the 1st and 2nd argument

#best way to print
name = input("What's your name? ")
print(f"hello, {name}")
output: hello, rik

#how to use quote inside a print
print('hello, "quote"')
output: hello, "quote"
#alternate the single and double quotes

#single quote
print("hello, 'quote'")
output: hello, 'quote'
#alternate the single and double quotes

#better way
print("hello, \"quote\"")
output: hello, "quote"

#remove whitespace from str
name = name.strip()
#ex:
name = input("What is your name? ")
#user input:        les
name = name.strip()
print(f"hello, {name}")
output: hello, les

#left strip or right strip
name = name.lstrip()
name = name.rstrip()

#Capitalize the first char
name = name.capitalize()
#Capitalize the first letter of each argument
name = name.title()

#It can be chained
name = name.strip().title()
#It can be simplified further
name = input("What is your name? ").strip().title()

#Lower or Up every letter
name = name.lower()
name = name.upper()

#Split
name = input("What is your name? ")
#Split user's name
#Only expects 2 values
first, last = name.split(" ")
print(f"Hello, {first}")
output: Hello, blood

#Split call index
name = input("What is your name? ")
#Split user's name
container = name.split(" ")
print(f"Hello, {container[0]}")

#Recap
x = int(input("What is x? "))
round(number[, ndigits])
#ex
z = round(x+y, 2)
#auto
z = round(x+y)

#with comma
print(f"{z:,}")

#round with printf
print(f"{z:.2f}")

def hello(to="world"):
	print("hello,", to)
hello()
name = input("What's your name?")
hello(name)
output:
hello, world
What's your name?
hello, David

"""