def is_prime(number):
    for x in range(2,int(number**(0.5))):
        if number % x == 0:
            return False
    return True

number = int(input())

print("Is prime :",is_prime(number))