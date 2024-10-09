if __name__ == '__main__':

    records = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records_temp = []
        records_temp.append(name)
        records_temp.append(score)
        scores.append(score)
        records.append(records_temp)
        
    scores.sort()
        
    lowest_score = scores[0]
    second_lowest = 0
        
    length = len(scores)
  
    for i in range(length):
        if scores[i] != lowest_score:
            second_lowest = scores[i]
            break
    
    second_low_list = []        
    for name, score in records:
        if score == second_lowest:
            second_low_list.append(name)
            
    second_low_list = sorted(second_low_list)
    
    for name in second_low_list:
        print(name)
                             
        
        
        
