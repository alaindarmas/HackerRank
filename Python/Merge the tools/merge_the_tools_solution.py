from collections import OrderedDict

def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        
        substring = string[i:i+k]
        u = ''.join(OrderedDict.fromkeys(substring))
        
        print(u)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)