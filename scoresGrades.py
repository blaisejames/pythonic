def scoresGrades():
    import random
    score = 0
    grade = ""
    print "Scores and Grades"
    for i in range(0, 10):
        score = random.randint(60, 100)
        if score >= 90:
            grade = "A"
        elif score >= 80 and score < 90:
            grade = "B"   
        elif score >= 70 and score < 80:
            grade = "C" 
        else:
            grade = "D" 
        print "Score: {}; Your grade is {}".format(score, grade)
    print "End of the program. Bye!"

scoresGrades()