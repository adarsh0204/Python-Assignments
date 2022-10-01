                                            #Assignment 2

#Q1: Write a python script to print types of variables. Create 5 variables each of them
#containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
'''
a=35
b=True
c="iam_adarsh04"
d=5.46
e=3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))'''

#Q2: Write a python script to print the id of two variables containing the same integer values.
'''
a=97
b=97
print(id(a))
print(id(b))'''

#Q3: Write a python script to print all the keywords.
'''
imp-ort keyword
print(keyword.kwlist)'''

#Q4: Write a python script to display the current date and time. First create variables to
#store date and time, then display date and time in proper format (like: 30-9-2022 and 9:00 PM)
'''
from datetime import datetime
dt=datetime.today()
print(dt)
d1=dt.strftime("%d-%m-%Y and %I:%M %p")
print(d1)
d2=dt.strftime("%B %d %Y")
print(d2)
d3=dt.strftime("%d/%b/%Y")
print(d3)'''



