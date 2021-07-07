# Lambda to sort list of Tuples
olist = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Old : ", olist)
olist.sort(key = lambda x:x[1])
print("New : ",olist)

# -------------------------------------------------------------------------------------
# Lambda to sort list of Dictionaries
odict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print("Old : ", odict)
odict.sort(key=lambda x:x["color"])
print("New : ", odict)

# -------------------------------------------------------------------------------------
# Lambda to filter list of integers : Even numbers & Odd numbers
allnumlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : x % 2 == 0,allnumlist))
odd = list(filter(lambda x : x % 2 != 0,allnumlist))
print("Even :", even)
print("Odd :", odd)

# -------------------------------------------------------------------------------------
# Remove None value from a given list
oldlist = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
print(oldlist)
# 1st way =>
a = list(filter(lambda i : i != None, oldlist))
print(a)
# 2nd way =>
def delnon(oldlist):
    return list(filter(lambda i : i != None, oldlist))
print(delnon(oldlist))

# -------------------------------------------------------------------------------------
# Add two Lists and build 3rd with Map and Lambda
l1 = [1, 2, 3]
l2 = [4, 5, 6]
z = list(map(lambda x,y : x+y,l1,l2))
print(z)
# -------------------------------------------------------------------------------------
# intersection of two given arrays
l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
z = list(filter(lambda x : x in l1,l2))
print(z)
# -------------------------------------------------------------------------------------