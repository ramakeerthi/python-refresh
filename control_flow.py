day = input("Enter day of the week it is")

# If and related statemenets

if day == "Monday":
    print("Have a great start of the week")
elif day == "Tuesday":
    print("It is tuesday")
else:
    print("Wait for weekend")


# In keyword

friends = {"The matrix","Green Book","Her"}

user_movie = input("Enter a movie that you have watched recently")

if(user_movie in friends):
    print("Your friends have also watched this movie recently")
else:
    print("None of your friends have watched this movie recently")
