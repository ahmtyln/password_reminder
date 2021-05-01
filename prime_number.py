def prime_number():
    x=input("enter a positif number")
    if x.isdigit():
        for i in range(2,int(x)):
            if int(x)%i==0:
                print(f"{x} is not a prime number")
                break
            else:
                print(f"{x} is a prime number")
                break
    else:
        print("Please enter a positif number")

prime_number()


