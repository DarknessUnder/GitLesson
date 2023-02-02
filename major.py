attendanceList = [["Harry Tan", "tant2", "DarknessUnder"]]

## add your info here
attendanceList.append(["Gabriel Jacob", "jacobggit", "????"])



## DO NOT CHANGE
printedList = open("RightAttendanceList.txt", "w") 

for i in range(len(attendanceList)):
    printedList.write( attendanceList[i][1] + "\n")

printedList.close() 