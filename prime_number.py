def prime_number():
    number = input("Enter a positif number please: ")
    while int(number) > 0 :
        for i in range(2,10):
            if int(number) % i != 0:
                return f"entered number is prime number"

print(prime_number())







# print(f"entered negatif number or zero number please try again")
