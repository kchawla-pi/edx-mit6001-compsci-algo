# def a(x, y, z):
#     if x:
#         return y
#     else:
#         return z
#
#
# def b(q, r):
#     return a(q > r, q, r)
#
# print(a(3>2, a, b))
#

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    product = 1
    while exp:
        product *= base
        exp -= 1
    return product

# base, exp = 5.5, 3
# print(base ** exp == iterPower(base, exp))


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
    
# result = recurPower(base, exp)
# print(result)
# print(base ** exp == result)

stack = {1: [], 2: [], 3: []}
stack[1] = [4, 3, 2, 1]

stack[2].append(stack[1].pop())
stack[3].append(stack[1].pop())
stack[3].append(stack[2].pop())

stack[2].append(stack[1].pop())
stack[1].append(stack[3].pop())

stack[2].append(stack[3].pop())
stack[2].append(stack[1].pop())

# stack = {1: [], 2: [], 3: []}
# stack[1] = [4, 3, 2, 1]
stack[3].append(stack[1].pop())
stack[1].append(stack[2].pop())
stack[3].append(stack[2].pop())

stack[2].append(stack[1].pop())
stack[1].append(stack[3].pop())
stack[1].append(stack[2].pop())
stack[3].append(stack[2].pop())
stack[2].append(stack[1].pop())
stack[3].append(stack[1].pop())
stack[3].append(stack[2].pop())



# stack2 = {1: [], 2: [], 3: []}
# stack2[1] = [2, 1]
#
# if len(stack2[1]) == 0 or stack2[1][-1] < stack2[2][-1]:
#     stack2[1].append(stack2[1].pop())
# elif len(stack2[2]) == 0 or stack2[2][-1] < stack2[1][-1]:
#     stack2[2].append(stack2[1].pop())
# elif len(stack2[3]) != 0 or stack2[3][-1] < stack2[1][-1]:
#     stack2[3].append(stack2[1].pop())

stack2 = {1: [], 2: [], 3: []}
stack2[1] = [2, 1]
for stack_ in [1, 2, 3]:
    for i in {1,2,3}.difference({stack_}):
        if len(stack2[stack_]) == 0 or stack2[stack_][-1] < stack2[i][-1]:
            stack2[stack_].append(stack2[i].pop())

print()
