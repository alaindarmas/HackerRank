from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    
    columns = input().split()
    Student = namedtuple('Student', 'ID MARKS NAME CLASS')
    

    col_mapping = {}
    for i, col in enumerate(columns):
        if col == 'ID':
            col_mapping['ID'] = i
        elif col == 'MARKS':
            col_mapping['MARKS'] = i
        elif col == 'NAME':
            col_mapping['NAME'] = i
        elif col == 'CLASS':
            col_mapping['CLASS'] = i
    
    marksTotal = 0
    for _ in range(n):
        row = input().split()
        currentStudent = Student(
            ID=row[col_mapping['ID']],
            MARKS=row[col_mapping['MARKS']],
            NAME=row[col_mapping['NAME']],
            CLASS=row[col_mapping['CLASS']]
        )
        marksTotal += int(currentStudent.MARKS)
        
        
    avgMarks = float(marksTotal/n)
    
    print(avgMarks)
