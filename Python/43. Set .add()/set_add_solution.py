if __name__ == "__main__":
    n = int(input())
    
    stamp_set = set()
    for _ in range(n):
        stamp = input().strip()
        
        stamp_set.add(stamp)
        
    print(len(stamp_set))
