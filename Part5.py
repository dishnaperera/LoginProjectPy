# After completing the program for the login, Christina Kaiser has asked for your assistance with another small job,
# fixing a program that was written by another trainee which is not correct.
# The trainee was asked to create an application that determines the average mark
# for a student based on their marks from five different subjects (see code below).
# The instructions stated that the application must do the following:
# •	Ask the user to input the marks for the five subjects in a list/array.
# •	The program must ensure that the marks are between 0 and 100
# •	Display the list/array of marks entered.
# •	Find the sum of all the marks in the list (all five subjects) and display the output as:
# ­	The sum of your marks is: [sum]
# •	Find the average of all the marks in the list (all five subjects) and display the output as:
# ­	The average of your marks is: [average mark]
#  

print("please enter your 5 marks below\n"
      "please enter number between 0-100")

#read 5 inputs
for x in range(1, 5):
    mark[x] = int(input("enter mark " + str(x)))

mark1 = int(input("enter mark 1: "))
mark2 = int(input("enter mark 2: "))
mark3 = int(input("enter mark 3: "))
mark4 = int(input("enter mark 4: "))
mark5 = int(input("enter mark 5: "))

#create array/list with five marks
marksList = [mark1, mark2, mark3, mark4, mark5]

#print the array/list
print(marksList)

#calculate the sum and average
sumOfMarks = sum(marksList)
averageOfMarks = sum(marksList)/5

#display results
print("The sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))
