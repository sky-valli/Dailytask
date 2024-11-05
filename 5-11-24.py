class college:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def display(self,branch):
        self.branch=branch
        print(self.name)
        print(self.branch)
    class student_details:
        student_section='A'
        def __init__(self,student_name,student_id):
            self.student_name=student_name
            self.student_id=student_id
            print(self.student_name)
            print(self.student_id)
        @staticmethod
        def display_inner(number):
            print (number * number)

name=input('enter college_name :')
age=int(input('enter branch:'))
coll = college(name,age)
new_display=input('enter branch :')
coll.display(new_display)
stu_name=input('enter student_name :')
stu_id=int(input('enter id:'))
d=int(input('enter number :'))
s = college.student_details(stu_id,stu_name)
s.display_inner(d)






    