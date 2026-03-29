# Loops and Iterations in Python.

# While loops
# While loop keeps running till the time the condition is TRUE.
# while condition:
#     print("Hello")

# attempts = 0
# max_attempts = 5

# while attempts < max_attempts:
#     attempts += 1
#     print(f"Attempt number: {attempts}")

# print("Loop Completed")

# count = 10

# while count > 0:
#     print(count)
#     count -= 1

# print("Loop Completed")

# While loop can also be used to take user input.
# age = int(input('PLease enter your age: '))

# # age > 0 and age <= 110
# while age < 0 or age > 110:
#     print("Invalid age, age must be between 0 to 110")
#     age = int(input('Please try again: '))

# print(f"Valid age: {age}")

# Example - Build a number guessing game.
# secret_number = 49
# guess = int(input("Please guess your number (1-100): "))

# while guess != secret_number:
#     if guess < secret_number:
#         print("please guess some higher number.")
#     else:
#         print("please guess some smaller number.")
#     guess = int(input("Please try again with a number (1-100): "))

# print("You have guessed the correct number.")

# Break Statement - Early termination. Exit loop before it's natural completion.

# attempts = 0
# max_attempts = 5
# correct_password = "masai"
# password = input("please enter your password: ")

# while attempts < max_attempts:
#     attempts += 1
#     print(f"Attempt number: {attempts}")    
    
#     if password == correct_password:
#         # no need to go to the next attempt, rather break the loop
#         print("Password is correct")
#         break

#     password = input("please try again: ")



# keys = ['kitchen', 'bedroom', 'garage', 'drawingroom', 'studyroom']

# for 

# count = 0

# while count < 10:
#     print(count)
#     if count == 5:
#         print("Breaking the loop....")
#         break # Exit the loop from here.

#     count += 1

# print("After loop.")

# Break - terminates the loop immediately and skips the remaining code in the loop.

# while True: 
#     password = input("Please enter your password:")
#     if password == 'secret':
#         print("Access granted")
#         break
#     print("Wrong password, please try again")

# while True:
#     age = int(input("Please enter your age: "))

#     if age < 0:
#         print("age can't be negative")
#     elif age > 120:
#         print("age can't be more than 120")
#     else:
#         #valid age
#         print(f"Valid age: {age}")
#         break

# continue - skips to the next iteration.
while True:
    age = int(input("Please enter your age: "))

    if age < 0:
        print("age can't be negative")
        continue
    
    if age > 120:
        print("age can't be more than 120")
        continue
    
    #valid age
    print(f"Valid age: {age}")
    break
    
    

    