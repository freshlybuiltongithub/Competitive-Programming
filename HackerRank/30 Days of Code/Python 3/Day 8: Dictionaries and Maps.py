"""
Hackerrank Solution for Day 8: Dictionaries and Maps
"""
n = int(input())
phonebook = {}
for i in range(n):
    a,b = input().split()
    phonebook[a] = b

while 1:
    try:
        q = input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:
        break

