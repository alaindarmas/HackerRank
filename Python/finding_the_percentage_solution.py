if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    x=0
    for i in student_marks[query_name]:
        x = x+i
    print("%.2f"%(x/len(student_marks[query_name])))
    
    