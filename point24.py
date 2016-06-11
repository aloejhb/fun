import numpy as np
import itertools


def operation(xy, op):
    ans = np.nan
    x = xy[0]
    y = xy[1]
    if op == '+':
        ans = x + y
    elif op == '-':
        ans = abs(x - y)
    elif op == '*':
        ans = x * y
    elif op == '/':
        mi, ma = sorted(xy)
        if mi != 0 and ma % mi ==0:
            ans = ma / mi
    return ans

def apply_ops(ab, cd, ops):
    ans = operation((operation(ab, ops[0]), operation(cd, ops[1])), ops[2])
    return ans
        
def try_partition(ab, cd):
    for ops in itertools.product('+-*/', repeat=3):
        ans = apply_ops(ab, cd, ops)
        if ans == 24:
            print ab, cd, ops
        
def point24(nos):
    a, b, c, d = nos
    try_partition((a,b), (c,d))
    try_partition((a,c), (b,d))
    try_partition((b,c), (a,d))
    
    
a = 8
b = 3
c = 2
d = 6

while 1:
    str = raw_input("Please enter 4 pos int, separated by comma:\n")
    if str == 'q':
        break
    else:
        nos = map(int, str.split(','))
        point24(nos)
