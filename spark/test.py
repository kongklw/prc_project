from random import random
import time

n = 100000 * 2

t1 = time.time()


def f(_):
    x = random() * 2 - 1
    y = random() * 2 - 1
    return 1 if x ** 2 + y ** 2 <= 1 else 0


count = 0
for i in range(1, n + 1):
    count += f("a")
t2 = time.time()

print("Pi is roughly %f" % (4.0 * count / n))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, ]

print(list(filter(lambda x: x % 3, a)))
print(list(map(lambda x, y: x * y, a, b)))
