#Unpacking used to destructure args/ reuse

# 1

def add(*args):
    return sum(args)

print(add(1,2,3,4,5,5,4))

# 2

def subtract(x,y):
    return x-y

nums = [10,5]
print(subtract(*nums))

# 3
dict_nums = {'y':5,'x':10}
print(subtract(**dict_nums))