import sys
from math import sqrt,pow #from math library import square root and power
import datetime  #library to make the date 

#The sys library connect php with python, so that "sys.argv[...]" is the order in the php.
b = int(sys.argv[1])#Put the parameters as an integer 
a = int(sys.argv[2]) #Put the parameters as an integer
c = int(sys.argv[3])#Put the parameters as an integer
result = b+(sqrt(c**3)/a)*10 #Here's the equation inside of "result" variable 

c_cubed = pow(c,3) #c cubed
sqrt_c_cubed = sqrt(c_cubed) #sqrt of the c cubed
division = sqrt_c_cubed / a #sqrt of the c cubed divided by a
mutiplication = division * 10 #sqrt of the c cubed divided by a multiplied by 10
addition = b + mutiplication #b plus the result of the previous step

print(f"the result of the equation is: {result}") #Print the result of the equation

print(f"step 1: c= {c} , c**3={c_cubed}") #Print the first step of the equation
print(f"step 2: sqrt(c**3) = {sqrt_c_cubed}") #Print the second step of the equation
print(f"step 3: c= {c} / a= {a} = {division}") #Print the third step of the equation
print(f"step 4: {(sqrt(c**3)/a)} * 10 = {mutiplication}") #Print the fourth step of the equation
print(f"step 5: {b} + {mutiplication}  = {result}") #Print the fifth step of the equation

print(f"This was made it on {datetime.datetime.now()}") #Print the date and time


