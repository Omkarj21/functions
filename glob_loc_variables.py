# Global variable inside Local Scope
# x = 2
# def varscop():
#     global x
#     x += 3
#     print(x)
# varscop()
# print(x*3)
# -------------------------------------------------
# Local variable with nonlocal keyword
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# Output without nonlocal
    # inner: nonlocal
    # outer: local
# Output with nonlocal
    # inner: nonlocal
    # outer: nonlocal
# -------------------------------------------------