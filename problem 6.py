#question 6
#import counter to be able to count number of letter grades earned
from collections import Counter

def letter_grade_and_point(numerical_score):
    if 85<= numerical_score<= 100:
        grade_letter="A+"
        grade_point=4

    elif 80<= numerical_score<= 84:
        grade_letter="A"
        grade_point=4
    

    elif 75<= numerical_score<= 79:
        grade_letter="B+"
        grade_point=3.5
        
    elif 70<= numerical_score<= 74:
        grade_letter="B"
        grade_point=3.00
        
    
    elif 65<= numerical_score<= 69:
        grade_letter="C+"
        grade_point=2.50
        
    elif 60<= numerical_score<= 64:
        grade_letter="C"
        grade_point=2
    
    
    elif 55<= numerical_score<= 59:
        grade_letter="D+"
        grade_point=1.50
        
    elif 50<= numerical_score<= 54:
        grade_letter="D"
        grade_point=1
        
    else:
        numerical_score<50
        grade_letter="E"
        grade_point=0.00
#store the grade letter and grade point in a list to be able to access each easily
    return[grade_letter,grade_point]

def honour_categorie(gpas):
    if 3.85<=gpas<=4.0:
        return ('Summa Cum Laude')
    elif 3.70<=gpas<=3.84:
        return("Magna Cum Laude")
    elif 3.50<=gpas<=3.69:
        return("Cum Laude")
    else:
        return ("you graduated without honors)
courses= int(input('enter the number of courses'))
#create an empty list for letter grades and weight
course_grade_letter=[]
grade_weight=[]
grade_applied_weight=[]
for i in  range (courses):
    score=float(input('enter numerical score earned in the course'))
    course_weight=float(input('enter weight of each course'))
    grade_and_point=(letter_grade_and_point(score))
#using append to put the results obtained into the empty list course_grade_letter[]
    course_grade_letter.append(grade_and_point[0])
#using append to put the results obtained into the empty list grade_weight[]
    grade_weight.append(course_weight)
    grade_applied_weight.append(grade_and_point[1]*course_weight)
    print(grade_and_point)


counter_grade = Counter(course_grade_letter)
for key,value in counter_grade.items():
      print( f" you have { value}", f"{key}s")
sum_weight = 0
for item in grade_weight:
    sum_weight = sum_weight+item
#initialize sum grade to 0 to start counting.
sum_grade =0
for grade in grade_applied_weight:
    sum_grade = sum_grade+grade
cum_gpa = sum_grade/sum_weight

print( "You've graduated with",honour_categorie(cum_gpa))
    


        
        
      
