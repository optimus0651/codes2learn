'''
Created on Dec 22, 2018

@author: Akash Nandy
'''
s = input()
val = list(map(int,input().split()))
max_xor = 1
calc_list = []

calc_list.append(val.pop())

while val:
    x = val.pop()
    while calc_list:
        n = calc_list.pop()
        max_xor = max(max_xor,x^n)
        if n > x :
            calc_list.append(n)
            break
print(max_xor)
        
