
if __name__ == "__main__":
    numE = int(input())
    
    english = set(input().split())
    
    numF = int(input())
    
    french = set(input().split())
    
    print(len(english.difference(french)))