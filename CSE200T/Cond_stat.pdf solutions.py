# #1
# # ▪ Write a program to convert entered temperatures to and from Celsius and Fahrenheit. 
# # Formula: C = 5/9 × (𝐹−32)
# unit = input("Enter the unit (C or F): ")
# temp = float(input("Enter the temperature: "))

# print(f'Input Temperature: {temp} {unit}')
# if unit == "F":
#     celsius = 5 /9 * (temp - 32)
#     print(f'Output Temperature: {celsius} C')
# elif unit == "C":
#     farenheit = (9/5 * temp) + 32
#     print(f'Output Temperature: {farenheit} F')
# else:
#     print("Invalid Inputs")

# #2
# # Write a program to calculate the  electricity bill of your last month  usage 
# # electricity unit which will be taken as user input using the following criteria: 

# user_input = int(input("Enter the electricity units used: "))
# bill = 0 

# if user_input <= 100:
#     bill = user_input * 2
# if user_input > 100 and user_input <= 200:
#     bill = (100 * 2) + ((user_input - 100) * 5)
# if user_input > 200 and user_input <= 500:
#     bill = (100 * 2) + (100 * 5) + ((user_input - 200) * 10)
# if user_input > 500:
#     bill = (100 * 2) + (100 * 5) + (300 *10) + ((user_input - 500) * 25)
# else:
#     print(user_input, "is not divisible by 3 or 5")
# print("Your total bill is: ", bill) #this code is errorfree


# #3 
# #Write a program to check whether the last digit of an entered number greater 
# #than 100 is divisible by 3 or 5. 

# user_input = int(input("Enter the number greater than 100: "))
# string1 = 0
# last_digit_int = 0

# if user_input > 100: # 5021
#     string1 = str(user_input)
#     last_digit = string1[-1]
#     last_digit_int = int(last_digit)
#     if last_digit_int % 3 == 0:
#         print(user_input, "is divisible by 3")
#     elif last_digit_int % 5 == 0:
#         print(user_input, "is divisible by 5")
# else:
#     print("Invalid number")

# #4
# #Write a program to calculate the fare of any destination from IUB using bike 
# # or car based on the following formula: 
# #Bike fare = Booking fee + 15 tk cost per-KM + 3 tk cost per-minute wait + 1 tk surcharge per-minute 
# #Car fare = Booking fee + 25 tk cost per KM + 5 tk cost per minute wait + 2 tk surcharge per-minute 
#  #Take necessary user input for doing the calculation.

# user_input = input("Enter vehicle (Bike/Car): ")
# user_input2 = int(input("Enter distance in KM: "))
# user_input3 = int(input("Enter wait time in minutes: "))

# fee = 0
# if user_input == "Bike":
#     fee = (15 * user_input2) + (3 * user_input3) + (1 * user_input3)
# if user_input == "Car":
#     fee = (25 * user_input2) + (5 * user_input3) + (2 * user_input3)
# print(f'The {user_input} fare for you is : Booking fee + {fee}')



    






