def amstrong_number():
    toplam=0
    while True:
         number=input("sayı giriniz: ")
         for i in number:
             if i == "-":
                 return f"It is an invalid entry. Don't use non-numeric, float, or negative values!"
             elif i== ".":
                 return f"It is an invalid entry. Don't use non-numeric, float, or negative values!"
             elif i.isdigit()== False:
                 return f"It is an invalid entry. Don't use non-numeric, float, or negative values!"
             else:
                 toplam+=int(i)**len(number)
         if toplam == int(number):
             return f"entered number is {int(number)} and an Armstrong number."
            
         else:
             return f"entered number is {int(number)} and not an Armstrong number."
                             
                 
print(amstrong_number())               

