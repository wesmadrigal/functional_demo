#!/usr/bin/env python

# Lambdas at a high level
"""
Lambdas are essentially anonymous functions that we define.
They originate from lambda calculus.  The term lambda has
different meanings depending on the field in which it is
used.  In Physics, they are related to wave length.

Example:

    square = lambda x: x**2
    square(4)
    16
 
    square(5)
    25


We can define lambdas the same way we can any other function
with respect to parameters.  Try an arbitrary number with
some logic.

Example:

    add_three = lambda x, y, z: x + y + z

    add_three(1, 2, 3)
    6

    add_three(4, 4, 4)
    12

"""

# The map builtin function
"""
Map essentially does what it says, it maps a function
to every item in an iterable.  So if we pass a function
to map and an iterable of arguments, we will get an
iterable of the results of the function back.  

Example:

    square = lambda x: x**2

    args = [1, 2, 3, 4]

    map(square, args)
    [1, 4, 9, 16]


    cube = lambda x: x**3

    args = [1, 2, 3, 4]
   
    map(cube, args)
    1, 8, 27, 64

"""


# Combining maps and lambas
"""
We already did this in the above, but rather than having
to define a function and then pass it to a map, why
not define it on the fly and map it?

Example:

    args = [1, 2, 3, 4]

    map(lambda x: x**2, args)
    [1, 4, 9, 16]


    map(lambda x: x**3, args)
    [1, 8, 27, 64]


These are the exact same as above, except we used the lambdas
how they are meant to be used, anonymously.
"""


# Reducers
"""
Reduce is a builtin function that does also what it's name says,
reduction.  Given a function to perform on the incoming args
and the previously contained one, reduce chops down iterables into
single values


Example:

    iterable = [1, 2, 3, 4]

    reduce(lambda x, y: x + y, iterable)
    10


What happened, internally, is this:

    (((1+2)+3)+4)

The reduce used our anonymous function to take it's current value
x and add the next in the sequence to it.  We can do this with
multiplication, division, whatever we ant.


Example 2:

    iterable = [1, 2, 3, 4]

    reduce(lambda x, y: x * y, iterable)
    24


What really happend:

    (((1*2)*3)*4)
    24

"""




def fib_reg(n):
    if n < 2:
        return n
    else:
        return fib_reg(n - 1) + fib_reg(n - 2)



# the exact same logic as the above
fib_func = lambda n: (n if n < 2 else fib_func(n - 1) + fib_func(n - 2))


import time
def factorial(n):
    if n < 2:
        return n
    else:
        return n * fact(n - 1)


# combining lambdas and reducers
fact = lambda n: reduce(lambda x, y: x * y, reversed(range(1, n + 1)))
"""
What's happening here:

   fact
      - assigned anonymous function 'lambda n' which takes 1 argument


   reversed(range(1,n+1))

      - range(1,n+1)
        [1,.... n+1]

      - reversed
        [n+1, ...., 1]

   
   reduce(lambda x, y: x * y
      - reducing down by multiplication
      - ( ( ( ( ( n+1 * n ) * n-1) * n-2) * ...) * 1)
       
"""


def trace(f):
    a = 1

    def helper(x, y, z):
        start = time.time()
        res = f(x, y, z)
        end = time.time()
        print 'Timing: {0}'.format(end - start)
        print a
        return res


    a += 1
    return helper



@trace
def compound_interest1(principal, interest, years):
    for i in range(years):
        gained = principal * (1.0 + interest) - principal
        principal += gained

    return principal


"""
This is pretty complex, but it does exactly the same thing as the above
"""
compound_interest2 = lambda principal, interest, years: reduce(lambda x, y: x + (x * y - x), map(lambda x: 1.0 + interest, range(years))) * principal





def memoize(f):
    cache = {}

    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]


    return helper


global_var = 'blah'

def test_fact(n):
    start = time.time()
    fact1 = factorial(n)
    end = time.time()
    start2 = time.time()
    fact2 = fact(n)
    end2 = time.time()
    print 'Test original: {0}\nTest functional: {1}'.format(end - start, end2 - start2)



def test_fib(n):
    fib1 = fib_reg(n)
    t1_time = end - start
    start1 = time.time()
    fib2 = fib_func(n)
    end1 = time.time()
    t2_time = end1 - start1
    start3 = time.time()
    fib3 = memoize(fib_reg)
    fib3_val = fib3(n)
    stop3 = time.time()
    t3_time = stop3 - start3
    print 'Regular fib: {0}\nFact Fib: {1}\nMemoize Fib: {2}'.format(t1_time, t2_time, t3_time)


