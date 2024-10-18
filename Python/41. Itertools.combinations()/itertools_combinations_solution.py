from itertools import combinations

if __name__ == "__main__":
    s, k = input().split()
    
    k = int(k)
    
    for i in range(1, k+1):
        for combination in combinations(sorted(s), i):
            print("".join(combination))
    
    
