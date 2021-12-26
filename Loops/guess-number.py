import random as rand

rand_number = rand.randint(1, 10)
print(rand_number)
count = 0

guessed = False

while guessed == False:
    print("your guess:")
    count += 1
    guessedNumber = int(input())
    if rand_number == guessedNumber:
        guessed = True

print(f"you guessed in {count} turns")
