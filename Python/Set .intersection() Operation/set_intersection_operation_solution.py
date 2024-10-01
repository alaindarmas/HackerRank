if __name__ == "__main__":
    n = int(input())
    
    n_set = set(input().split())
    
    b = int(input())
    
    b_set = set(input().split())
    
    print(len(n_set.intersection(b_set)))