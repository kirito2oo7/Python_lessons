def convert_cel_to_far(number):
    return round(number * 9/5 + 32,2)

def convert_far_to_cel(number):
    return round((number - 32) * 5/9,2)

number = int(input("Enter a temperature in degrees F: "))
print(f"{number} degrees F = {convert_far_to_cel(number):.2f} degrees C")

number2 = int(input("Enter a temperature in degrees C: "))
print(f"{number2} degrees C = {convert_cel_to_far(number2):.2f} degrees F")