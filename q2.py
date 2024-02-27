numbers = [1, 2, 3, 4, 5, 6, 7]
res = [x * x for x in numbers]
print(res)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2]
print(res)
