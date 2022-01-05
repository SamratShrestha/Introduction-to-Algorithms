from functools import reduce, partial
from itertools import count

print(list(map(lambda x,y: x+y+2, range(10),range(5))))
print(list(map(print,range(10),range(5))))

print(list(filter(lambda number : number % 2 == 0 , range(10))))
print(reduce(lambda x,y:x+y,range(10)))

# for i in count():
#     print(i)

power_of_2 = partial(pow,2)

print(power_of_2(5))


def fibonacci():
    a,b =  0,1
    while True:
        yield b
        a, b = b, a+b

fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
