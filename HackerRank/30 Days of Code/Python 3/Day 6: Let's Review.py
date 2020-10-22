"""
Hackerrank Solution for Day 6: Let's Review
"""
n = int(input())


for i in range(n):
    flag = 0
    e = ""
    o = ""
    a = input()
    for j in a:
        if flag == 0:
            e=e+j
            flag =1
        else:
            o = o + j
            flag = 0
    print(e,o)

