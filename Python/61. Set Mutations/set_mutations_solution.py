if __name__ == "__main__":
    n_A = int(input())
    
    a = set(map(int, input().split()))
    
    n = int(input())
    
    for _ in range(n):
        
        fullOperationName = input().split()
        
        operationName = fullOperationName[0]
        
        set_operation = getattr(a, operationName)
        
        otherSetElements = set(map(int, input().split())) 
        
        set_operation(otherSetElements)
    
    
    print(sum(a))