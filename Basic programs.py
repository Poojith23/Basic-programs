#!/usr/bin/env python
# coding: utf-8

# In[16]:


num1 = 15
num2 = 12
 
# Adding two nos
sum = num1 + num2
 
# printing values
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))



# Python3 program to add two numbers
 
number1 = input("First number: ")
number2 = input("\nSecond number: ")
 
# Adding two numbers
# User might also enter float numbers
sum = float(number1) + float(number2)
 
# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))



# Driver Code
if __name__ == "__main__" :
  num1 = int(input("Enter the number:"))
  num2 = int(input("Enter the number:"))
   
  # Adding two numbers
  sum_twoNum = lambda num1, num2 : num1 + num2
   
  # printing values
  print("Sum of {0} and {1} is {2};" .format(num1, num2, sum_twoNum(num1, num2)))


# In[15]:


#Maximum of two numbers in Python

# Python program to find the
# maximum of two numbers
 
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
     
# Driver code
a = 9
b = 7
print(maximum(a, b))


# Python program to find the
# maximum of two numbers
 
a = 1
b = 3
maximum = max(a, b)
print(maximum)# Driver code

# maximum of two numbers
a = 2
b = 7
# Use of ternary operator
print(a if a >= b else b)


# python code to find maximum of two numbers
 
a=5;b=10
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')


# maximum of two numbers
#Using list comprehension
a=3;b=9
x=[a if a>b else b]
print("maximum number is:",x)


# In[19]:


#Python Program for simple interest

# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
    si = (p * t * r)/100
    print('The Simple Interest is', si)
    return si
     
# Driver code
simple_interest(8, 6, 8)


#Python Program for compound interest
 
def compound_interest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
# Driver Code
compound_interest(10000, 10.25, 5)


#Finding compound interest of given values without using pow() function.
# Python code
# To find compound interest
# inputs
p= 1200   # principal amount
t= 2      # time
r= 5.4    # rate
# calculates the compound interest
a=p*(1+(r/100))**t  # formula for calculating amount
ci=a-p  # compound interest = amount - principal amount
# printing compound interest value
print(ci)


# In[ ]:




