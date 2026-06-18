# Vansh garg

#Q1 

n, r, p = 10, 5, 100
A = p*(1 + (r/100))**n
print(A)  #Ans = 162.89


#Q2
A2 = 10
B2 = 20
Str = "There are {} students in class, with {} who play at least one sport."

print(Str.format(B2,A2))


#Q3
print("It goes without saying, \"Time is Money\", and none can deny it.")


#Q4
x = lambda a,b:a//b
print(x(10,3)) #ans = 3


#Q5
A5 = 10
B5 = 12
print("Smaller") if A5 == B5 else print("Greater") if A5<B5 else print("True")

#Ans = Greater


#Q6 
import os
import numpy
my_list = [1,2,2,3]
print(my_list)
arr = numpy.array(my_list, dtype = int)
print(arr)
