"""
### Question 2:
Please create a function which will take two integers as parameters and will return the subtraction of them.
eg.: 

```Python
> my_subt_func(5,3)
> 2"""

def my_subt_func(a,b):
    return (a-b)

num1 = int(input('First number:'))
num2 = int(input('Second number:'))

print(my_subt_func(num1,num2))
