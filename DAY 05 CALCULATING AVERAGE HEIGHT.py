student_heights =input("Enter heights of students in class:\n").split()
sum1=0
count=0
for i in range(0,len(student_heights)):
    student_heights[i]=int(student_heights[i])
    sum1+=student_heights[i]
    count+=1
average_height=round(sum1/count)
print(f"Number of students are: {count}\n")
print(f"Average height of students is:{average_height}")


