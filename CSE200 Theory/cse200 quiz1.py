'''
Make a function shape(n) which will make a shape where the odd rows give "+" 
and even rows give "-" and the number of entries increase every row.
For example, def(5) gives the shape:

+
- -
+ + +
- - - -
+ + + + +

'''
#ans:

def shape(n):
    for i in range(n):
        if i % 2 == 0: 
            for j in range(n - i):
                print("+", end=" ")
        if i % 2 == 1:
            for j in range(n - i):
                print("-", end=" ")
        print()
        
shape(5)

'''
Make a function diffTwoThreeMult(a,b) which will calculate the difference between 
the sum of the multiples of 2 and the sum of multiples of 3 within the specified range (a,b).
For example, Difference between the sum of multiples of 2 and 3 within range (2,10):
(2+4+6+8+10) - (3+6+9) = 12
Sample:

diffTwoThreeMult(2,10)
returns 12 
'''

def diffTwoThreeMult(a,b):
    sum2 = 0
    sum3 = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            sum2 += i
        if i % 3 == 0:
            sum3 += i
    return sum2 - sum3

print(diffTwoThreeMult(2,10))

#output>> 12


