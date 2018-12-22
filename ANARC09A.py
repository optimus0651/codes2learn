'''
Created on Dec 22, 2018

@author: Akash Nandy
'''
test = True
test_count = 0

brac_list = list(input())

while test:
    
    test_count += 1
    r = l = count = 0
    
    for x in brac_list:
        
        if x == '{':
            r +=1
            
        if x == '}':
            if r > 0:
                r -= 1
            else:
                l += 1
                

    if r&1 :
        count += int(r/2) + 1
    else:
        count += int(r/2)
        
        
    if l&1 :
        count += int(l/2) + 1
    else:
        count += int(l/2)
    
    
    print(str(test_count)+'.'+ ' '+str(count))
    
    brac_list = list(input())
    if brac_list[0] == '-':
        test = False
    
    