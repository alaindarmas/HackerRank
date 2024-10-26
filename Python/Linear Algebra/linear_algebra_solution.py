import numpy as np

if __name__ == "__main__":
    n = int(input())
    
    arr = []
    
    for _ in range(n):
        currentValue = list(map(float, input().split()))
        arr.append(currentValue)
        
    arr = np.array(arr)
    
    determinant = round(np.linalg.det(arr),2)
    
    print(float(determinant))
        
