print("Welcome to the Grade Sorter App")

#Create Empty Grades List
gradelist = []

#get grade inputs
grade = int(input("\nWhat is your first grade (0-100)?"))
gradelist.append(grade)
grade = int(input("What is your second grade (0-100)?"))
gradelist.append(grade)
grade = int(input("What is your third grade (0-100)?"))
gradelist.append(grade)
grade = int(input("What is your fourth grade (0-100)?"))
gradelist.append(grade)

#output results
print("\nYour grades are:" + str(gradelist))
gradelist.sort(reverse=True)
print("\nYour grades from highest to lowest are:" + str(gradelist))
print("\nThe 2 lowest grades will now be dropped.")
Removed_grade = gradelist.pop()
print("Removed grade:" + str(Removed_grade))
Removed_grade = gradelist.pop()
print("Removed grade:" + str(Removed_grade))

print("\nYour remaining grades are: " + str(gradelist))
print("Nice work! Your highest grade is a " + str(gradelist[0]))
