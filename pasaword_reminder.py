password_list = {"ahmet" : "123",
                 "ali" : "1234",
                 "mehmet" : "1234@",
                 "murat"  : "12345!"}

name = input("enter your name for learning password: ").lower()

if name in password_list:
    print(f"Hello, {name}! The password is : {password_list[name]}")
else:
    print(f"Hello, {name}! See you later.")


