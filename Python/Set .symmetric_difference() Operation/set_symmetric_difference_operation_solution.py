if __name__ == "__main__":
    
    e = int(input())
        
    english_set = set(input().split())
        
    f = int(input())
        
    french_set = set(input().split())
        
    print(len(english_set.symmetric_difference(french_set)))
            