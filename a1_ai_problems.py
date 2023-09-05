# Complete your individualized AI problems here

# def fizbuzz(input_num):
#     if(input_num%3==0):
#         if(input_num%5==0):
#             return 'FizzBuzz'
#         return 'Fizz'
#     elif(input_num%5==0):
#         return 'Buzz'
#     else:
#         return input_num

# assert fizbuzz(1) == 1, "fizzbuzz 1 test"
# assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
# assert fizbuzz(4) == 4, "fizzbuzz 4 test"
# assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
# assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
# assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# 1. Palindrome Checker:**
# Write a program that checks if a given string is a palindrome (reads the same forwards and backwards).

pali = "dessert"
drone = ''.join(list(reversed(pali)))

if pali == drone:
    print("They natch!")
else
    print("Try again!")


# **19. Basic Password Generator:**
# Write a program that generates a random password with a specified length.
# import random 
# passLength = input("How long do you want your password to be?")
# password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', '1', '2', '3', '4', '5', '6', '7', '8']
# rand = random.choice(password)
# print(rand)

