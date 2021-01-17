# The user give a number and the programm return 2 square
# one full and one empty.

n = int(input("Gimme a number: "))

count= 0

for i in range(n):
    count += 1
    if count== 1 or count== n:
        print(n* "*" + "  " + n* "*")
    else:
        print(n* "*" + "  " + "*" + (n -2) * " " +"*")
