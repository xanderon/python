fizz = "Fizz"
buzz = "Buzz"
for nr in range(1, 101):
    if nr % 3 == 0 and nr % 5 == 0:
        print(f"{fizz}{buzz}")
    elif nr % 3 == 0:
        print(fizz)
    elif nr % 5 == 0:
        print(buzz)
    else:
        print(nr)
