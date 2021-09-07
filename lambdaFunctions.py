# EXERCISES

'''
1. Write a Python program to create a lambda function that adds 15 
to a given number passed in as an argument, also create a lambda 
function that multiplies argument x with argument y and print the result.

Sample Output:
25
48
'''
print("Exercise 1")

add_fifteen = lambda x: x+15
print(add_fifteen(10))

multiply = lambda x, y: x*y
print(multiply(6, 8))

'''
2. Write a Python program to create a function that takes one argument, 
and that argument will be multiplied with an unknown given number. 

Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
'''

print("Exercise 2")

def multiply(factor):
    return lambda number: factor * number

double = multiply(2)
print("Double the number of 15 = ", double(15))

triple = multiply(3)
print("Triple the number of 15 = ", triple(15))

cuadruple = multiply(4)
print("Cuadruple the number of 15 = ", cuadruple(15))

quintuple = multiply(5)
print("Quintuple the number of 15 = ", quintuple(15))

'''
3. Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

print("Exercise 3")

# Syntax list.sort(reverse=True|False, key=myFunc) 
# reverse Optional. reverse=True will sort the list descending. Default is reverse=False
# key Optional. A function to specify the sorting criteria(s)

original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(original_list)

original_list.sort(key = lambda x: x[1])
print("Sorting the List of Tuples:")
print(original_list)

'''
4. Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

print("Exercise 4")

original_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Original list of dictionaries :")
print(original_list)

original_list.sort(key = lambda x:x['color'])
print("Sorting the List of dictionaries :")
print(original_list)

'''
5. Write a Python program to filter a list of integers using Lambda.

Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

print("Exercise 5")

original_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(original_list)

even_list = list(filter(lambda x: x % 2 == 0, original_list))
print("Even numbers from the said list:")
print(even_list)

odd_list = list(filter(lambda x: x % 2 != 0, original_list))
print("Odd numbers from the said list:")
print(odd_list)

'''
6. Write a Python program to square and cube every number in a given list of integers using Lambda.

Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''

print("Exercise 6")

original_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(original_list)

square_list = list(map(lambda x: x * x, original_list))
print("Square every number of the said list:")
print(square_list)

cube_list = list(map(lambda x: x * x * x, original_list))
print("Cube every number of the said list:")
print(cube_list)

'''
7. Write a Python program to find if a given string starts with a given character using Lambda.

Sample Output:
True
False
'''

print("Exercise 7")

starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('A') else False
print(starts_with('Python'))

'''
8. Write a Python program to extract year, month, date and time using Lambda.

Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178
'''

print("Exercise 8")

import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

'''
9. Write a Python program to check whether a given string is number or not using Lambda. 

Sample Output:
True
True
False
True
False
True
Print checking numbers:
True
True
'''

print("Exercise 9")

string_is_number = lambda x: True if x.isnumeric() else False

print(string_is_number("19"))
print(string_is_number("14"))
print(string_is_number("6 años"))
print(string_is_number("11"))
print(string_is_number("Martes 13"))
print(string_is_number("16"))
print("Print checking numbers:")
print(string_is_number("10"))
print(string_is_number("31"))

'''
10. Write a Python program to create Fibonacci series upto n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

print("Exercise 10")

from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("Fibonacci series upto 5:")
print(fib_series(5))
print("Fibonacci series upto 6:")
print(fib_series(6))
print("Fibonacci series upto 9:")
print(fib_series(9))

'''
11. Write a Python program to find intersection of two given arrays using Lambda. 

Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]
'''

print("Exercise 11")

first_array = [1, 2, 3, 5, 7, 8, 9, 10]
second_array = [1, 2, 4, 8, 9]
intersect = list(filter(lambda x: x in first_array, second_array))

print("Original arrays:")
print(first_array)
print(second_array)
print("Intersection of the said arrays:", intersect)

'''
12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
'''

print("Exercise 12")

original_array = [-1, 2, -3, 5, 7, 8, 9, -10] 
# La función anónima "crea" un nuevo valor para ordenar los elementos 
# Quedaría     = [1, -1/2, 1/3, -1/5, -1/7, -1/8, -1/9, 1/10]
# Usa el inverso aditivo y multiplicativo del número!
rearrange_array = sorted(original_array, key = lambda x: 0 if x == 0 else -1/x)

print("Original arrays:")
print(original_array)
print("Rearrange positive and negative numbers of the said array:")
print(rearrange_array)

'''
13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.

Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5
'''

print("Exercise 13")

original_array = [1, 2, 3, 5, 7, 8, 9, 10]

# Sin lambda

def count_even_odd(lista):
    even = 0
    odd = 0
    for n in lista:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

print(count_even_odd(original_array))

# Con lambda

even = len(list(filter(lambda x: x % 2 == 0 , original_array)))
odd = len(list(filter(lambda x: x % 2 != 0 , original_array)))

print("Original arrays:")
print(original_array)
print("Number of even numbers in the above array:", even)
print("Number of odd numbers in the above array:", odd)

'''
14. Write a Python program to find the values of length six in a given list using Lambda.

Sample Output:
Monday
Friday
Sunday
'''

print("Exercise 14")

six_len = list(filter(lambda x: len(x) == 6, ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]))

print("Sample Output:")
for i in six_len:
    print(i)

'''
15. Write a Python program to add two given lists using map and lambda.
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]
'''

print("Exercise 15")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x+y, list1, list2))

print("Original list:")
print("[1, 2, 3]")
print("[4, 5, 6]")
print("Result: after adding two list")
print(result)

'''
16. Write a Python program to find the second lowest grade of any student(s) from the 
given names and grades of each student using lists and lambda. Input number of students, 
names and grades of each student. 

Input number of students: 5
Name: S ROY
Grade: 1
Name: B BOSE
Grade: 3
Name: N KAR
Grade: 2
Name: C DUTTA
Grade: 1
Name: G GHOSH
Grade: 1
Names and Grades of all students:
[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
Second lowest grade: 2.0
Names:
N KAR
'''




 