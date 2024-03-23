friend_ages = {"Adam":24, "Nate":35, "Bob":60}


for friend in friend_ages:
    print(f"{friend} is {friend_ages[friend]} years old")


for friend,age in friend_ages.items():
    print(f"{friend} is {age} years old")

values = [age for age in friend_ages.values()]
print(values)