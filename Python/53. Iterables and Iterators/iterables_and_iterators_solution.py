import itertools 

def main():
    n = int(input())
    newList = list(input().split())
    k = int(input())
    
    combinations = list(itertools.combinations(range(n), k))
    totalCombinations = len(combinations)
    
    
    presentCombinations = 0
    
    for combo in combinations:
        if any(newList[i] == 'a' for i in combo):
            presentCombinations = presentCombinations + 1
    
    probability = presentCombinations / totalCombinations
    
    
    print(f"{probability:.3f}")
    
    
if __name__ == "__main__":
    main()