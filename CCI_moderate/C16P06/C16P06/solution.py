def smallest_dif(a, b):
    a.sort()
    b.sort()
    N = len(a)
    M = len(b)
    
    ans = abs(a[0] - b[0])
    
    i = j = 0
    
    
    while i < N and j < M:
        
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] <= b[j]:
            i += 1
        else:
            j += 1
            

        
    return ans