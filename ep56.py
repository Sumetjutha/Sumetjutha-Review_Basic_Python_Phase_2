### Factorial

########################################################################################################################

def factorial(number):
    if number == 1:
        return number
    else :
        return number * factorial(number -1)

x = factorial(8)
print("ผลลัพธ์ของ factorial => ",x)
########################################################################################################################