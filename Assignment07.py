#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate how Pickling works
#              Demonstrate how structured error handling works
# ChangeLog (Who,When,What):
# JDSmith,3.2.20,Created file
# JDSmith,3.4.20,Seeded with sample code
# JDSmith,3.5.20,Pickling demo
# ---------------------------------------------------------------------------- #
# import pickle
#
# print("Let's make a list to pickle.")
# color1 = input('Give me a color: ')
# color2 = input('Give me a second color: ')
# color3 = input('Give me a third color: ')
# shape1 = input('Give me a shape: ')
# shape2 = input('Give me a second shape: ')
# shape3 = input('Give me a third shape: ')
# color = [color1, color2, color3]
# shape = [shape1, shape2, shape3]
# print("Pickling two lists into a binary file, shapes.dat...")
# file = open("shapes.dat", "wb")
# pickle.dump(color, file)
# pickle.dump(shape, file)
# file.close()
# print("If you go open shapes.dat, it looks like junk inside. That's because it's not meant for humans to read,"
#       " just computers.")
# print("\nUnpickling lists from shapes.dat...")
# file = open("shapes.dat", "rb")
# color = pickle.load(file)
# shape = pickle.load(file)
# file.close()
# print('Here is the information that was pickled.')
# print(color)
# print(shape)
# print('The information that was pickled is now a list in memory, and you can mix it up however you like:')
# print(color[0], shape[2] + ', ' + color[2], shape[1] + ', ' + color[1], shape[0])
# print("That's pickling, another way to write and read data.\n")
# # TODO: try exceptions
# print('#' * 40 + '\n')
# # Demonstrate handling exceptions
# # try/except
# print('We can deal with errors. Built in stuff from Python, and stuff we can make up.')
# specifying exception type
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("Good job, you entered a number. Next time, try typing in a word instead, to see an error.")
#
# # handle multiple exception types
# print()
# for value in (None, "Hi!"):
#     try:
#         print("Attempting to convert", value, "-->", end=" ")
#         print(float(value))
#     except (TypeError, ValueError):
#         print("Something went wrong!")
#
# print()
# for value in (None, "Hi!"):
#     try:
#         print("Attempting to convert", value, "-->", end=" ")
#         print(float(value))
#     except TypeError:
#         print("I can only convert a string or a number!")
#     except ValueError:
#         print("I can only convert a string of digits!")
#
# # get an exception's argument
# try:
#     num = float(input("\nEnter a number: "))
# except ValueError as e:
#     print("That was not a number! Or as Python would say...")
#     print(e)
#
# # try/except/else
# try:
#     num = float(input("\nEnter a number: "))
# except ValueError:
#     print("That was not a number!")
# else:
#     print("You entered the number", num)
#
# input("\n\nPress the enter key to exit.")

# Data -------------------------------------------- #

# Processing -------------------------------------- #

# Presentation ------------------------------------ #
