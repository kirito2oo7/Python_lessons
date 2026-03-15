universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(list_of_university):
    total_student = 0
    total_tuition = 0
    for university in list_of_university:
        total_student += university[1]
        total_tuition += university[2]

    return [total_student , total_tuition]


def mean(list_of_university):
    total_student_mean = enrollment_stats(universities)[0] / len(list_of_university)
    total_Tuition_mean = enrollment_stats(universities)[1] / len(list_of_university)
    return [total_student_mean , total_Tuition_mean ]

def median(list_of_university):
    list_student = []
    for i in list_of_university:
        list_student.append(i[1])

    list_student.sort()
    student_median = list_student[len(list_student)//2]

    list_Tuition  = []
    for j in list_of_university:
        list_Tuition.append(j[2])

    list_Tuition.sort()
    Tuition_median = list_Tuition[len(list_Tuition)//2]

    return [student_median , Tuition_median]


txt = f"""******************************
Total students: {enrollment_stats(universities)[0]}
Total tuition: $ {enrollment_stats(universities)[1]}

Student mean: {mean(universities)[0]:.2f}
Student median: {median(universities)[0]}

Tuition mean: $ {mean(universities)[1]:.2f}
Tuition median: $ {median(universities)[1]}
******************************"""

print(txt)