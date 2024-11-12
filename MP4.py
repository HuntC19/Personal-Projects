#
#Machine Project 4
#
#Hunter Cataldo
#
#Description: This code is made up of 6 functions that each have
#their own responsibility (description in body of function). This
#code prints out players names and their 3 test scores along with
#their test averages and sorts them according to how you call the
#functions.
#

def getScores():

    #
    # Opens the data file of names and scores... firstName, lastName, score1,
    # score2, score3... reads each line of data as a str, divides the line into
    # the 5 values... str, str, int, int, int... puts those values in a list,
    # and returns a list of those lists.
    #
    # There are no parameters.
    #
    # Returns a list of lists... each list contains a str, str, int, int, int.
    #
    scores = []
    with open("1300 - MP4 Data.txt") as myFile:
        for line in myFile:
            data = line.split()
            data[2] = int(data[2])
            data[3] = int(data[3])
            data[4] = int(data[4])
            scores.append(data)
    return scores


def addTestAverage(studentScores):

    #
    # Finds the average of each student's test scores, and then appends that
    # average onto the end of that student's list. So, each student list now
    # contains str, str, int, int, int, float.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int which are firstName, lastName, test1, test2,
    # test3.
    #
    # There is no return value.
    #
    for student in studentScores:
        average = sum(student[2:5]) / 3
        student.append(average)


def calcTotals(studentScores):

    #
    # Finds the average of test1, test2, test3, and the total average. Returns
    # those 4 values in a list.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    #
    # Returns a list with 4 values... float, float, float, float... which are
    # test1 avg, test2 avg, test3 avg, total avg.
    #
    test1_total = sum(student[2] for student in studentScores) / len(studentScores)
    test2_total = sum(student[3] for student in studentScores) / len(studentScores)
    test3_total = sum(student[4] for student in studentScores) / len(studentScores)
    test_total_avg = sum(student[5] for student in studentScores) / len(studentScores)
    return [test1_total, test2_total, test3_total, test_total_avg]


def printScores(studentScores, totals):

    #
    # Prints out the entire list including firstName, lastName, score1, score2,
    # score3, average. There is a header for each column. The totals are
    # printed at the end.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    # totals A list of 4 float values... the averages for test1,
    # test2, test3, and totalAverage.
    #
    # There is no return value.
    #
    print(f"{'Name':<20} {'Exam1':>7} {'Exam2':>7} {'Exam3':>7} {'Avg':>7}")
    for student in studentScores:
        print(f"{student[0] + ' ' + student[1]:<20} {student[2]:>7} {student[3]:>7} {student[4]:>7} {student[5]:>7.2f}")
    print(f"{'Total':<20} {totals[0]:>7.2f} {totals[1]:>7.2f} {totals[2]:>7.2f} {totals[3]:>7.2f}")
    print()


def sortByName(studentScores):

    #
    # Sorts the list of student info by the student's last name. Uses the
    # Bubble Sort algorithm.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    #
    # There is no return value.
    #
    for i in range(len(studentScores) - 1):
        for j in range(len(studentScores) - 1):
            if studentScores[j][1] > studentScores[j + 1][1]:
                temp = studentScores[j]
                studentScores[j] = studentScores[j + 1]
                studentScores[j + 1] = temp

def sortByAverage(studentScores):

    #
    # Sorts the list of student info by the test average. Uses the
    # Bubble Sort algorithm.
    #
    # studentScores A list of lists, each list contains a str, str, int,
    # int, int, float which are firstName, lastName, test1,
    # test2, test3, average.
    #
    # There is no return value.
    #
    for i in range(len(studentScores) - 1):
        for j in range(len(studentScores) - 1):
            if studentScores[j][5] < studentScores[j+1][5]:
                temp = studentScores[j]
                studentScores[j] = studentScores[j+1]
                studentScores[j+1] = temp


studentScores = getScores()
addTestAverage(studentScores)
totals = calcTotals(studentScores)
printScores(studentScores, totals)
sortByName(studentScores)
printScores(studentScores, totals)
sortByAverage(studentScores)
printScores(studentScores, totals)