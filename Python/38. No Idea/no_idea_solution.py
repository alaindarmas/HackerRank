def main():
    sizes = input().split()
    
    n = int(sizes[0])
    m = int(sizes[1])
    
    initial_arr = list(map(int, input().split()[:n]))
    
    set_a = set(map(int, input().split()[:m]))

    set_b = set(map(int, input().split()[:m]))
    
    happiness = 0
    

    for item in initial_arr:
        if item in set_a:
            happiness += 1
        if item in set_b:
            happiness -= 1
        
    print(happiness)
    
if __name__ == "__main__":
    main()
    
    

    
    
    
