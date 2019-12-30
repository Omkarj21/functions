# Python Arbitrary Arguments
# ------------------------------------------------------
# Python **kwargs
def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="omkar", Lastname="jadhav", Age=27, Phone=1234567890)
intro(Firstname="vinay", Lastname="lonkar", Email="vinaylonk@gmail.com", Country="India", Age=28, Phone=9881234567)
# ---------------------------
# Python *args
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:", sum)
adder( 3, 5 )
adder( 4, 5, 6, 7 )
adder( 1, 2, 3, 5, 6 )
# ---------------------------------------------------------------------------------