print("Please answer the question like 'Yes' or 'No'")
age=input("Are you a cigarette addict older than 75 years old? : ").lower()
chronic=input("Do you have a severe chronic disease? : ").lower()
immune=input("Is your immune system too weak? : ").lower()

def covid(a):
    if a == "yes":
        return True
    else:
        return False

risk = covid(age) or covid(chronic) or covid(immune)
if risk==True:
    print("You are in risky group")
else:
    print("You are not in risky group")

