# Python Grade Calculator by Jesus Monroy IV

#Declaring variables
num_lab_probs = float(input("How many lab programming problems are completed?"))
num_quiz_class = float(input("How many quizzes and in-class activities are completed?"))

grade_assignment1 = float(input("What is the grade of Assignment 1? ")) * 0.04
grade_assignment2 = float(input("What is the grade of Assignment 2? ")) * 0.04
grade_assignment3 = float(input("What is the grade of Assignment 3? ")) * 0.04
grade_assignment4 = float(input("What is the grade of Assignment 4? ")) * 0.04

grade_midterm1 = float(input("What is the grade of Midterm 1? ")) * 0.125
grade_midterm2 = float(input("What is the grade of Midterm 2? ")) * 0.125

grade_finalexam = float(input("What is the grade of the Final Exam? ")) * 0.18
grade_midterm_final_prep = float(input("What is the grade of the midterm and final preparation? ")) * 0.06

grade_lab_probs = 0
grade_quiz_class = 0

#Verifying lab and quiz numbers, then calculating their weighted grades
if num_lab_probs >= 6:
    grade_lab_probs = 20.0
else:
    grade_lab_probs = num_lab_probs / 6 * 100 * 0.2
if num_quiz_class >= 6:
    grade_quiz_class = 15.0
else:
    grade_quiz_class = num_quiz_class / 6 * 100 * 0.15

#Calculating total weighted grade
total_grade = round(grade_lab_probs + grade_quiz_class + grade_assignment1 + grade_assignment2 + grade_assignment3 + grade_assignment4 + grade_midterm1 + grade_midterm2 + grade_finalexam + grade_midterm_final_prep)

print("Your grade is " + str(total_grade))
