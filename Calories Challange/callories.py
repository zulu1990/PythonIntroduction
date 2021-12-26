print("Today's Date: ")
todayDate = input()

print("Breakfast calories: ")
breakfast = int(input())

print("Lunch calories: ")
lunch = int(input())

print("dinner calories: ")
dinner = int(input())

print("snuck calories: ")
snuck = int(input())

sum = breakfast + lunch + dinner + snuck

print("Calorie content for " + todayDate + ":" + str(sum))