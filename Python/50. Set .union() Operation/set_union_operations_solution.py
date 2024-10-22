if __name__ == "__main__":
    n = input()
    
    english = set(input().split())
    
    b = input()
    
    french = set(input().split())
    
    print (len(english.union(french)))