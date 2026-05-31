print('student management system')
print('1 = add student')
print('2= update student')
print('3=remove student')
print("4= search student")
student_list=[]
try:
    choice=int(input('enter choice: '))
  

    if 5<=choice or choice==0:
        print('not a valid choice')
    else:
        print('well')
except ValueError:
    print('please enter a valid choice')

if choice==1:
    total_student=int(input('enter no of student you are going to deal = '))
    i=0
    for student in range(total_student):
        student=input(f'{i+1}student name : ')
        roll_no=int(input(f'{i+1}student rollno : '))
        i+=1
        print('work successfuly done!')
        student_data={'name':student,
                    'roll_no':roll_no}
        student_list.append(student_data)
        print(student_list)

elif choice==2:
    print("pick either student or roll_no for search student.")
    print('if you not know the student name then give a tab space')
    print("if you enter student name then you can just pass 0 to roll_no.")
    student_name=input('student name : ') 
    if student_name in student_list:
        print("found student")
    else:
        roll_no=int(input('roll_no: '))
        if  roll_no in student_list:
            print('found')
        else:
            print('not present in data')
            pass
    print(student_name)
elif choice==3:
    print (student_list)
    name=input('enter student name = ' )
    remove.name
    print(student_list)

