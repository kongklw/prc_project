def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 2))


def add_end(L=[]):
    L.append('END')
    return L


print(add_end(['1', '2', '3']))
print(add_end(['1', '2', '3', 4, 5]))
print(add_end(['1', '2', '3']))

print(add_end())
print(add_end())
print(add_end())
print(add_end([1, 2, 3, 4, 5, 6, 7]))

x = 1
y = x

print(x is y)


