student_name=input("Enter your name:")
USN=input("Enter your USN:")

marks1= int(input("Enter marks in subject 1:"))
marks2= int(input("Enter marks in subject 2:"))
marks3= int(input("Enter marks in subject 3:"))

total_marks=marks1+marks2+marks3
average_marks=total_marks/3

print("Student Name:",student_name)
print("USN:",USN)
print("course 1 marks:",marks1)
print("course 2 marks:",marks2)
print("course 3 marks:",marks3)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)
percentage=(total_marks/300)*100
print("Percentage:",percentage,"%")
