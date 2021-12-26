print("want to continue? ")

answer = input()

if answer.lower() == "yes":
    print("Continuing..")
    print("Complete!")
elif answer.lower() == "no":
    print("Exiting")
else:
    print("Please try again and respond with yes or no.")