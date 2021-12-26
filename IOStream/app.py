employees_file = open("IOStream/employees.txt", "r")
print(employees_file.readline()) #reads 1 line
print(employees_file.readline()) #reads 1 line
print(" --- ")

print(employees_file.read()) # reads whole file

employees_file.close()

#=======================================

employees_file = open("IOStream/employees.txt", "a")

employees_file.writelines

employees_file.close()

# "r" read file
# "a" appends file new data
# "w" creates new file or overwrites existing file
