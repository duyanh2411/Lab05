tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)
