from functools import reduce

num = [1,2,3,4]

a =list(map(lambda x: x + 1, num))
print(a)

a =list(map(lambda x: x * x, num))
print(a)

a = list(filter(lambda x: x % 2 == 0, num))
print(a)

# a = list(reduce(lambda x, y: x + y, num))
a = reduce((lambda x, y: x + y), num)
print(a)

lines = ['heheh heeheh ;e;e lelell']
points = list(map(lambda line: line.split()[2], lines))
print(points)