# factorial of a number parsing arguments from cmdline by iteration and by recursion

import sys

def fact_iter(x):


    if x<0:
        print('Invalid Input')
        quit()
    elif x==0:
        n=1
    else:
        n=1
        while x>0:
            n=n*x
            x=x-1
    print('Factorial by iteration:', n)


def fact_recs(x):
    if x < 0:
        print('Invalid Input')
        quit()
    elif x == 0:
        return 1
    else:
        return x*fact_recs(x-1)



x = int(sys.argv[1])
fact_iter(x)
y = fact_recs(x)
print('Factorial by Recursion:', y)
