if __name__ == "__main__":
    n = int(input())  
    
    wordDictionary = {}
    orderOfAppearance = []
    
    for _ in range(n):
        word = input().strip()  
        if word in wordDictionary:
            wordDictionary[word] += 1 
        else:
            wordDictionary[word] = 1   
            orderOfAppearance.append(word)  
    
    
    print(len(orderOfAppearance))
    
    
    for word in orderOfAppearance:
        print(wordDictionary[word], end=' ')        
