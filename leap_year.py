def leap_year():
    num = int(input("how many time which you want to ask: "))
    i=0
    while num>i:
        i+=1 
        year=int(input("you enter a year which want to define the year is leap year or not: "))
        if (year % 4 == 0) and (year % 100 != 0):
            print(f"{year} is a leap year")
        elif (year % 400 == 0) and (year % 100 == 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")      
leap_year()