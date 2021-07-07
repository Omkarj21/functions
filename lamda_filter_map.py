from functools import reduce
# While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.
# Syntax = lambda arguments: expression
# A lambda function can take any number of arguments, but can only have one expression.
# -----------------------------------------------------------------------
# showing difference between def() and lambda().
def cube(y):
    return y * y * y
g = lambda x: x * x * x
print("Lambda Output :",g(3)) # Lambda Output : 27
print("Def Output :",cube(5)) # Def Output : 125
# -----------------------------------------------------------------------
# Program to filter out only the even items from a list
# Filter =>
my_list1 = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list1))
# Output: [4, 6, 8, 12]
print("filter_lambda :",new_list)

# Map =>
my_list2 = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: (x % 2 == 0), my_list2))
# Output: [False, False, True, True, True, False, False, True]
print("map_lambda_No-Modify :",new_list)
# -----------------------------------------------------------------------
# Map =>
my_list3 = [1, 5, 4, 6, 8, 11, 3, 12]
# Program to double each item in a list using map()
new_list = list(map(lambda x: x * 2, my_list3))
# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print("map_lambda_Modify :",new_list)
# -----------------------------------------------------------------------
# Reduce =>
my_list4 = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = reduce((lambda x, y: x + y), my_list4)
print("reduce_lambda :",new_list)
# -----------------------------------------------------------------------
