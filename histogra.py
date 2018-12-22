

hist = list(map(int,input().split()[1:]))
k = s = len(hist)
big_pos = [None]* s  

big_pos[s-1] = 1
s-=2
prev = max = hist.pop()

while hist:
    x = hist.pop()
    if x< prev:
        big_pos[s] = big_pos[s+1]+1
    else :
        big_pos[s]=1
        
    if big_pos[s]*x > max :
        max = big_pos[s] * x
    s-=1
    prev = x
      
    
print(big_pos)
print(max)