student_score=input("Enter List of score of students: \n").split()
for i in range(0, len(student_score)):
    student_score[i]=int(student_score[i])
print("Score of students is class is:\n")
print(student_score)
maximum=int(student_score[0])
for n in range(0,len(student_score)-1):
    if maximum<=int(student_score[n+1]):
               maximum=student_score[n+1]


print(f"Maximum Score in list is: {maximum}")

        
        
    
    
