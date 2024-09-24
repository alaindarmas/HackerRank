
from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int,input().split())
    d = defaultdict(list)
    positionList = []
    
    for _ in range(n):
        char = input().strip()
        d['A'].append(char)
        
    for _ in range(m):
        char = input().strip()
        d['B'].append(char)
        
    for b_item in d['B']:
        found = False
        a_positions = []
        current_position = 1
        
        for a_item in d['A']:
            if a_item == b_item:
                a_positions.append(current_position)
                found = True
            current_position += 1
                
        if found == False:
            a_positions.append(-1)
            
        positionList.append(a_positions)
        
    for positions in positionList:
        print(" ".join(map(str, positions)))
            
                
                
            
