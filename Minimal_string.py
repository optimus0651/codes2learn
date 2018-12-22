'''
Created on Dec 22, 2018

@author: Akash Nandy
'''

def is_smallest(lst,pr,s):
    
    j = ord(s) - ord('a')
    
    for i in range(0,j):
        if lst[i]>0:
            return False
    return True
    

inp_str = list(input())
res = ''
alpha = [0]*26
qu = []

for i in range(0, len(inp_str)):
    j = ord(inp_str[i])-ord('a')
    alpha[j] += 1


for x in inp_str:
    
    qu.append(x)
    k = ord(x)-ord('a')
    alpha[k] -= 1
    while is_smallest(alpha,qu, x):
        res += qu.pop()
        if not qu:
            break
        x = qu[-1]

while qu:
    res += qu.pop()
    
print(res)