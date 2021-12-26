import random as rand

rand_number = rand.randint(1, 100)
print(rand_number)
count = 0

guessed = False

while guessed == False:
    count += 1
    guessed_number = int(input())
    if(guessed_number > rand_number) :
        print("your guess is too hight")
    elif(guessed_number < rand_number) :
        print("your guess is too small")
    else:
        guessed = True
        print("great guess!!")
else:
    print(f"it took {count} try to guess")