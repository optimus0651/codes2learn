'''
Created on Dec 20, 2018

@author: Akash Nandy
'''

t = int(input())

while t>0 :
    
    res = ''
    l = int(input())
    
    n = list(map(int,input().split(' ')))
    
#    for i in range(0,l):
#         n.append(int(input()))
    l-=1
    j=l 
    while l>=0 :
        if n[l] > n[l-1] :
            temp = n[l]
            n[l] = n[l-1]
            n[l-1] = temp
            res += str(n[l])
            break
        else :
            res += str(n[l])
            j-=1
        l = l-1
    
    l-=1        
    while l>=0:
        res += str(n[l])
        l-=1
        
    res = res[::-1]
    
    if j==0 :
        print(-1)
    else:
        print(int(res))
    
    t = t-1
        
        
        
        