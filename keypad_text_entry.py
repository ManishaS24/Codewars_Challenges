keys_available = ["1", "ABC2", "DEF3", "GHI4", "JKL5", "MNO6", "PQRS7", "TUV8", "WXYZ9", "*", " 0", "#"]

def presses(phrase):
    total_count = 0
    
    for i in phrase.upper():
        #print(i)
        for s in keys_available:
            #print(keys_available.index(s))
            idx = s.find(i)
            if idx == -1:
                continue
            else:
                #print(idx)
                total_count += s.index(i) + 1
    print(total_count)
                
            
    

presses('R U ALL R8') #- 2+1 + 1+1 + 0+1+2+1+2+1 + 2+1+3+1 = 19