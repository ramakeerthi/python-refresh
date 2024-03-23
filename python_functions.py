def user_age_in_seconds(age_in_years):
    return age_in_years*365*24*60*60

age = int(input("Enter age in years"))
print(user_age_in_seconds(age))

def say_hello(name,surname="DOg"):
    print(f"Hello, {name} {surname}")

say_hello(name="John")