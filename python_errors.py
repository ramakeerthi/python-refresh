def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    
    return dividend/divisor


try:
    print(divide(1,2))
except ZeroDivisionError:
    print("Cannot do this operation")
finally:
    print("Code is completely executed")
