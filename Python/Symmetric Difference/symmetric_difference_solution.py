
if __name__ == "__main__":
    set_M = set()
    set_N = set()
    
    m = int(input())
    
    set_M = set(map(int, input().split()))
        
    n = int(input())
    
    set_N = set(map(int, input().split()))
        
    m_difference = set_M.difference(set_N)  
    n_difference = set_N.difference(set_M)  
    
    final_difference = set()
    
    final_difference.update(m_difference)
    final_difference.update(n_difference)
    
    final_difference = sorted(final_difference)
    
    for value in final_difference:
        print(value)