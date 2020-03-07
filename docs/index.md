##### Pickling and Exceptions

###Introduction

In this module, we learned about using storing and extracting data from a binary file with the Pickle library, and various methods for dealing with errors using try/except. The script I wrote is a basic demonstration of using Pickle and some exception handling, based on internet research and our textbook.

###Pickling Research and Demo

I thought the best places to start looking would be our textbook and Python.org. The textbook was much friendlier than Python.org (Python.org, https://docs.python.org/3/library/pickle.html 2020)(external site). I also appreciated the work of a computational linguist at the University of Pittsburgh (Python 3 Notes, https://www.pitt.edu/~naraehan/python3/pickling.html 2020)(external site). 

For the example, I started with the sample code in our textbook (Dawson, Python Programming for the Absolute Beginner, Third Edition 2010)(Pp. 200-202). Here's the starter code (Figure 1).
![Figure 1](Screen%20Shot%202020-03-05%20at%2010.04.07%20PM.png)
Then I made the list-building more interactive (Figure 2).
![Figure 2](Screen%20Shot%202020-03-05%20at%2010.33.40%20PM.png)
Once that was working well, I added descriptions of what was happening and information about binary files(Figure 3).
![Figure 3](Screen%20Shot%202020-03-05%20at%2010.59.46%20PM.png)

###Exceptions Research and Demo

Exceptions are a huge topic. After reviewing our textbook, the listings from class, and various websites, I decided to restrict the demo to built-in exception BaseException sub-classes and the Exception class(Python.org, https://docs.python.org/3/library/exceptions.html#bltin-exceptions 2020)(external site). 
For the example, I started with the sample code in our textbook (Dawson, Python Programming for the Absolute Beginner, Third Edition 2010)(Pp. 207). Here's a first pass at the ValueError sub-class (Figure 4).
![Figure 4](Screen%20Shot%202020-03-05%20at%2011.22.14%20PM.png)
I set up the try/except twice so that users would definitely see an error state (Figure 5).
![Figure 5](Screen%20Shot%202020-03-06%20at%206.19.45%20PM.png)
In the next section, I demonstrated the Exception class by asking an important question (Figure 6).
![Figure 6](Screen%20Shot%202020-03-06%20at%206.21.20%20PM.png)
The output demonstrates the custom text string, the docstring that belongs to the Exception class, and a type query to show that Exception is a Python class.

###Running the Demo Script

The script ran in Terminal as expected. First the pickling section (Figure 7), then the Exceptions section (Figure 8).
![Figure 7](Screen%20Shot%202020-03-06%20at%207.33.14%20PM.png)
![Figure 8](Screen%20Shot%202020-03-06%20at%207.36.31%20PM.png)

###Conclusion

Pickling is a fast and flexible way to write and read data into compact files. Exception handling in Python is relatively simple to implement, but the subject is large enough to cover several assignments. I learned that the Python.org documentation is a good reference for me, but only after learning concepts elsewhere.
