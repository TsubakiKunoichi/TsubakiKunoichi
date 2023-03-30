
import math

#-------------------------------------------------------------------------------------------------
# First do a Python tutorial:
# https://python.land/python-tutorial

print ("hello world");
print ('A semicolon is not neccessary but more readable.')

#-------------------------------------------------------------------------------------------------
# Topics (more links to single lesons) are found in
# https://python.land/introduction-to-python

#-------------------------------------------------------------------------------------------------
# https://python.land/introduction-to-python/the-repl
# Python.exe can be excecuted via command promt if the path to the .exe is specified
#   in my case: C:\Kurisu_Programme\Python>python
#   install packages like numpy
#   ín my case: C:\Kurisu_Programme\Python\Scripts>pip install numpy
#A session may be ende with "exit()". After that close shell with "exit"

'''Interesting observation. different floatings after excecuting simple operation via command prompt 
4**2.3
24.251465064166364
4**2*4**0.3
24.251465064166368
'''

#-------------------------------------------------------------------------------------------------
#Funktionengrundlagen
# https://python.land/introduction-to-python/variable

result = 3*4+12
print('result = ', result);
result = int (5/2);
print('result = ', result)

# Force typing
# currently doesnt do anything. If forced by compiling a precompiler of specific IDE's are needed
# https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b
from typing import Dict
result: int
result = 4**3.1
print('result = ', result, 'with type ', type(result));
print('result = Booleans, with type ', type(True), "and comparison operators ==, !=, >, < \n especially True==1 and False==0, " 
      + "Test: ", True == 4);
print('logical operators are "not" "and" "or"')


#-------------------------------------------------------------------------------------------------
# https://python.land/introduction-to-python/python-for-loop
i=0; w = "";
for j in "World":
    i=i+1;
    w = w+j+j
print("w = ", w);
print( f"Why should I use f to prin variables like {i} and {i+1}?");

#-------------------------------------------------------------------------------------------------
# https://python.land/introduction-to-python/functions
def fib(a,b):
    print(a+b)
    return a+b
print("Fibonacchi sequence: Values till 1000")
a=0; b=1;
while a < 1000:
    a=fib(a,b)
    b=fib(b,a)

print("My favorite for loop")
string = ""; counter = "";
for i in range(2**4):
    string = string + str(i)
    if i==10:
        print(f"oh i is {i}")
    else:
        counter = counter + "."
else: print("results: ", string, " and ", counter)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------