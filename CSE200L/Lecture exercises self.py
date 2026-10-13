# #Exercises from Lecture_1_Week_1_Conditional_Statements.ipynb

# #Example
# purchase_amount = float(input("Enter the purchase amount: "))
# if purchase_amount > 50000:
#     discount = purchase_amount * (22 / 100)
# elif purchase_amount < 50000 and purchase_amount >= 40000:
#     discount = purchase_amount * (20 / 100)
# elif purchase_amount < 40000 and purchase_amount >= 25000:
#     discount = purchase_amount * (10 / 100)
# else:
#     discount = 0

# print(f'Discount amount is: {discount} and payable amount is: {purchase_amount - discount}')

# Lecture_2_Week_2_Loops_Part_1.ipynb

# number_limit = 5
# number = 0
# sum = 0 

# while number < number_limit:
#     sum += number
#     number += 1
# print(sum)

# #print  sum of first 5 natural numbers using while loop:

# sum = 0
# num = 5
# count = 0

# while count < num:
#     if count < 4:
#         print(count, end= "+")
#     else:
#         print(count, end= "=")
#     sum += count  #0, 
#     count += 1    #1
# print(sum)
#output: 0+1+2+3+4=10


# #using for loops:

# for i in range(5):
#     sum += i 
#incomplete


# #**Exercise: 4** Write a Python Program to find the sum of series 1^1+2^2+3^3...+N^N

# N = int(input('Enter End Number: '))
# number = 1
# sum = 0
# while number <= N:
#     if number < N:
#         print(f'{number}^{number}', end ="+")
    
#     else:
#         print(f'{number}^{number}', end= "=")

#     sum += pow(number,number)
#     number += 1

# print(sum)

# #**Exercise: 5** Write a Python program to display the n terms of odd natural number and their sum.
# #Sample Output:
# #Enter end number: 10
# #1 + 3 + 5 + 7 + 9 += 25

# num = int(input('Enter End Number: '))
# sum = 0
# count = 0

# while count < num:
#     if count % 2 != 0:
#         sum += count
#         print(count, end= "+")
#     else:
#         print(count, end= "=")
#     count += 1

# print(sum)


# #Lecture_3_using_string.ipynb (exercises)
# #ex1
# string1 = "I am the best in Python!! and I mean it. I will achieve A in this course for sure"
# print(string1) 
# print(string1[:13])
# print(string1[-33:-24])

# #ex 4
# v1 = int(input("Enter an integer:"))
# v2 = float(input("Enter a float:"))
# add = v1 + v2

# print (type(v1))
# print (type(v2))
# print (f'The sum of the integer and float is: {add} and the type of the sum is: {type(add)}')

# #ex 8
# q_mark = float(input("Enter an integer:"))
# l_mark = float(input("Enter an integer:"))

# if q_mark > l_mark and l_mark >= 6.5:
#     print("You will get bonus marks")
# else:
#     print("No bonus marks")

# #conditional statements
# #ex1

# salary = 15000
# bonus =  (15000 * (10 / 100))
# overtime = float(input("Enter the number of overtime hours: "))

# if overtime > 10:
#     total_salary = salary + bonus
#     print(f"Total salary with bonus: {total_salary}")
# else:
#     print(f"Total salary without bonus: {salary}")

# #nested conditional statements
# a = 18
# if a % 2 == 0:
#     if a % 3 == 0:
#         print(a, "is a multiple of 6 ")
#     else:
#         print(a, "is a multiple of 2 but not a multiple of 6")
# else:
#     print(a, "is not a multiple of 2")

# Lecture_2_Week_3_Loops_Part_2.ipynb











