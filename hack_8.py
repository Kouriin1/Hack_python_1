"""
list: [1,3,5,7,9] output => [3,5,7]
       0 1 2 3 4
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    del result[0]
    del result[-1]
    return result  

print(fn_hack_8())