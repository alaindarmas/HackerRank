if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a = int(input())
        
        a_set = set(input().split())
        
        b = int(input())
        
        b_set = set(input().split())
        
        if a_set.issubset(b_set):
            print(True)
        else:
            print(False)
        
        