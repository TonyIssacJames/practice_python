'''
a small piece of code to check if pylint3 will
warning if reduce() does not have default value
'''


from functools import reduce




LIST1 = list(map(int, input().split()))

if LIST1: #unless this is a list we cannot test for None, map returns an object
    RESULT = reduce(lambda x, y: x + y, LIST1)

print(RESULT)
