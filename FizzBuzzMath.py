# Program to showcase the Fizz Buzz gam

temp = 0
numbers = [*range(0, 101)]
fizz = float(input("Hello! What multiples would you like to replace with Fizz?\n"))

buzz = float(input("Hello! What multiples would you like to replace with Buzz?\n"))

for x in numbers:
    if (temp % fizz == 0):
        if (temp % buzz and temp % fizz == 0):
            numbers[temp] = "BuzzFizz"
        else:
            numbers[temp] = "Fizz"
    if (temp % buzz == 0):
        numbers[temp] = "Buzz"
    temp = temp + 1

numbers_string = str(numbers)
print("From 0 to a 100, the game Fizz Buzz would go like " + numbers_string)
