def main():
    setA = set(map(int,input().strip().split()))
    
    n = int(input())
    
    
    strictSuperset = True
    
    for _ in range(n):
        currentSet = set(map(int,input().strip().split()))
            
        isStrictSuperset = setA.issuperset(currentSet) and setA != currentSet
        
        if isStrictSuperset == False:
            strictSuperset = False
            break
        
    print(strictSuperset)  
    
if __name__ == "__main__":
    main()
    