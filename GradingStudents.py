import sys

grades = [73, 38, 67, 33]
newGrades = grades

def solve(grades):
    for i in range(len(grades)):
        temp1 = (grades[i]/5)+1
        temp2 = temp1*5
        diff = abs(temp2 - grades[i])
        if grades[i] < 38:
            newGrades[i] = grades[i]
        else:
            if diff<3:
                newGrades[i] = temp2

    return newGrades



result = solve(grades)
print result