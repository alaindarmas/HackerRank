import math

if __name__ == "__main__":
    k = int(input())
    
    roomList = list(map(int, input().split()))
    
    roomSize = len(roomList)
    
    groupAmt = math.floor(roomSize/k)
    
    roomList = sorted(roomList)
    
    captainRoom = 0
    
    i = 0
    while i + k <= len(roomList):  
        current_room = roomList[i]
        compare_room = roomList[i + k - 1]
        
        if current_room != compare_room:
            captainRoom = roomList[i]
            break
        else:
            i += k  
    else:
        captainRoom = roomList[-1]  

    print(captainRoom)
    
    
