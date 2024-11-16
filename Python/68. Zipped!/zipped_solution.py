def main():
    numberOfStudents, numberOfGrades = map(int, input().split())
    
    startingGrades = [0] * numberOfStudents
        
    for _ in range(numberOfGrades):
        grades = list(map(float, input().split()))
        
        if len(grades) != numberOfStudents:
            print("Error: Number of grades entered does not match the number of students.")
            return
        
        startingGrades = [x + y for x, y in zip(startingGrades, grades)]
        
    startingGrades = [grade / numberOfGrades for grade in startingGrades]
        
    for grade in startingGrades:
        print(f"{grade:.2f}")

if __name__ == "__main__":
    main()
