#  List comprehension

nums = [1,7,5,213]

doubled = [num*2 for num in nums]
print(doubled)

friends = ["Sam", "Samantha", "Rob", "Bob"]

starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)