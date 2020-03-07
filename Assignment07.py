#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate how Pickling works
#              Demonstrate how structured error handling works
# ChangeLog (Who,When,What):
# JDSmith,3.2.20,Created file
# JDSmith,3.4.20,Seeded with sample code
# JDSmith,3.5.20,Pickling demo
# JDSmith,3.6.20,Exception handling
# ---------------------------------------------------------------------------- #
import pickle

print("Let's make a list to pickle.")
color1 = input('Give me a color: ')
color2 = input('Give me a second color: ')
color3 = input('Give me a third color: ')
shape1 = input('Give me a shape: ')
shape2 = input('Give me a second shape: ')
shape3 = input('Give me a third shape: ')
color = [color1, color2, color3]
shape = [shape1, shape2, shape3]
print("\nPickling two lists into a binary file, shapes.dat...")
file = open("shapes.dat", "wb")
pickle.dump(color, file)
pickle.dump(shape, file)
file.close()
print("\nIf you go open shapes.dat, it looks like junk inside. That's because it's not meant for humans to read,"
      " just computers.")
print("\nUnpickling lists from shapes.dat...")
file = open("shapes.dat", "rb")
color = pickle.load(file)
shape = pickle.load(file)
file.close()
print('\nHere is the information that was pickled:')
print(color)
print(shape)
print('\nThe information that was pickled is now a list in memory, and you can mix it up however you like:')
print(color[0], shape[2] + ', ' + color[2], shape[1] + ', ' + color[1], shape[0])
print("\nThat's pickling, another way to write and read data.\n")
print('#' * 80 + '\n')
# Demonstrate handling exceptions
# try/except
print('We can deal with errors. Python has built in exceptions, '
      'and an Exception class we can use with custom arguments.')
print('There are many standard exceptions in Python, which you can find here: '
      'https://docs.python.org/3/library/exceptions.html#bltin-exceptions')
print('This example uses the built in ValueError.')
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("Good job, you entered a number. Next time, try typing in a word instead to see an error.")

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered a number, so you won't see the error.\n")

print('At the next prompt, try entering some words to see the use of the Exception class that is built into Python.\n')
try:
    everything = input("What is the meaning of Life, the Universe, and Everything? ")
    if everything.isnumeric():
        print("\nDirections were ignored. Let's pretend you typed some words.\n")
        raise Exception('Something went wrong.')
    else:
        raise Exception('Maybe you should ask Deep Thought.')
except Exception as e:
    print(e)
    print("\nException output: ")
    print(f'The custom Exception text is "{e}"\nThe docstring for the Exception class is "{e.__doc__}"\nAnd the type is {type(e)}')

