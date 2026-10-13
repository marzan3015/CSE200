# #Find prime or not using loops

# N = int(input("Enter a number: "))
# isPrime = True
# for a in range(2, N):
#     if N % a == 0:
#         isPrime = False
#         break
# if N < 2:  #To consider about 0 and 1 as both are not prime
#         isPrime = False

# if isPrime == True:
#     print("Number is prime")
# else:
#     print("Number is not prime")

# # Write a program to get the Fibonacci series betweeen 0 and 50

# n = 50
# count1 = 1
# count2 = 1

# for i in range(0, 51):
#     print(count1, end= " ")

#     count1, count2 = count2, count1 + count2

# # Using loops, output this shape-
# '''
# *
# * *
# * * *
# * * * *
# * * * * * 
# * * * *
# * * * 
# * * 
# *
# '''

# for i in range(0, 5):
#     for j in range(i + 1):
#         print("*", end= " ")
#     print()

# for k in range(4):
#     for l in range(4, k, -1): #k = 0,1,2,3,4
#         print("*", end= " ")
#     print()

