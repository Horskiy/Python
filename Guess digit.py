import random

magick_number = random.randint(1, 1000)
user_number = int(input("Enter your number: "))

while magick_number != user_number:

    if magick_number <= user_number:
        print("Less!!")
    else:
        print("Bigger!")
    user_number = int(input("Enter your number: "))

print("Your win!!")
