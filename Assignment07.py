#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate how Pickling works
#              Demonstrate how structured error handling works
# ChangeLog (Who,When,What):
# JDSmith,3.2.20,Created file
# JDSmith,3.4.20,Seeded with sample code
# ---------------------------------------------------------------------------- #
import pickle
# TODO: pickle.dump, pickle.load
color1 = input('give me a color: ')
color2 = input('give me a second color: ')
color3 = input('give me a third color: ')
shape1 = input('give me a shape: ')
shape2 = input('give me a second shape: ')
shape3 = input('give me a third shape: ')
color = [color1, color2, color3]
shape = [shape1, shape2, shape3]
print("Pickling two lists into a binary file")
file = open("shapes.dat", "wb")
pickle.dump(color, file)
pickle.dump(shape, file)
file.close()

print("\nUnpickling lists.")
file = open("shapes.dat", "rb")
color = pickle.load(file)
shape = pickle.load(file)
print(color)
print(shape)

file.close()
# TODO: try exceptions
# Handle It
# Demonstrates handling exceptions

# try/except
# try:
#     num = float(input("Enter a number: "))
# except:
#     print("Something went wrong!")
#
# # specifying exception type
# try:
#     num = float(input("\nEnter a number: "))
# except ValueError:
#     print("That was not a number!")
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
