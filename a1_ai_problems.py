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
#Write a program that checks if a given string is a palindrome (reads the same forwards and backwards).

pali = input("Enter a word! ")
drone = ''.join(list(reversed(pali))) ## reverses the string 

if pali == drone:
    print("They match!")
else:
    print("They don't match!")


# # **19. Basic Password Generator:**
# # Write a program that generates a random password with a specified length.
import random 
pass_length = int(input("How long do you want your password to be? "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', '1', '2', '3', '4', '5', '6', '7', '8']
random.shuffle(letters) ## shuffles the letters 

if len(letters) > pass_length: ## shortens letters based on number from pass_length 
    letters = letters[:pass_length] # makes letters equal to pass length

letters = ''.join(letters) ## gets rid of the [] and , between characters

print(letters)

# **7. Guess the Number:**
# Implement a simple number guessing game where the program generates a random number and the user tries to guess it.
rand_num = random.randint(1, 10)
correct_guess = False ## this boolean helps the game restart each time 

while not correct_guess: 
    guess = int(input("Guess the number! It's between 1 and 10. "))

    if guess == rand_num:
        correct_guess = True
        print("Hooray! You win!")
    else:
        print("Wrong, try again!")

# **6. Temperature Converter:**
#Create a program that converts temperatures between Fahrenheit and Celsius.
temp_c = int(input("How many degrees is it in Celsius? "))
fahrenheit = (temp_c * 9/5) + 32
print("It is " + str(fahrenheit) + " degrees today.")

temp_f = int(input("How many degrees is it in Fahrenheit? "))
celsius = (temp_f - 32) * (5/9)
print("It is " + str(celsius) + " degrees today.")


# **16. Vowel and Consonant Counter:**
#Write a program that counts the number of vowels and consonants in a given string.
vowel = ['a', 'e', 'i', 'o', 'u', 'y']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

word = input("What word would you like to input? ")

vowel_count = 0
consonant_count = 0 

for vow in word:
    if vow in vowel:
        vowel_count += 1

for con in word:
    if con in consonant:
        consonant_count += 1

print(f"The word has {vowel_count} vowels and {consonant_count} consonants")


# **8. Hangman Game:**
#Create a text-based Hangman game where a player tries to guess a hidden word letter by letter.
import random
h_words = ["hello", "blue", "ribbon", "cricket"]
h_words = random.choice(h_words)
print(h_words)

looper = False ## this boolean helps the game restart each time 

while not looper: 
    ask = input("Guess the first letter: ")

    if ask == h_words:
        looper = True
        print("Keep going!")
    else:
        print("Incorrect")





