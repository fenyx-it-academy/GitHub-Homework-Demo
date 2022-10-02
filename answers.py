### Question 1:
#Please create a function which will take two integers as parameters and will return the sum of them.
#eg.: 

#```Python
#> my_sum_func(1,2)
#> 3
#```


### Question 2:
#Please create a function which will take two integers as parameters and will return the subtraction of them.
#eg.: 

#```Python
#> my_subt_func(5,3)
#> 2
#```

### Question 1:
def sum_func(num1, num2):
    sum = num1 + num2
    return sum

num1 = 1
num2 = 2
print(sum_func(num1, num2))

### Question 2:
def subt_func(num1, num2):
    subt = num1 - num2
    return subt

num1 = 5
num2 = 3
print(subt_func(num1, num2))