# Write a programm , that gives you back how many digits
# are composing the n number.

def digits(n):
    if n<0:
        return "negative"
    elif n<10:
        return 1
    else:
        return digits(n // 10) + 1
