class student:
    def __init__(self, name, className, rollNo):
        self.name = name
        self.className = className
        self.rollNo = rollNo
	
    def __repr__(self):
	    return f"student(|Name : {self.name}|, |class : {self.className}|, |rollNo : {self.rollNo}|)"

class school:
    def __init__(self):
        self.students = []
    def add(self, Student):
        self.Student = Student
        self.students.append(self.Student)
    def removeStudent(self, rollNum):
        self.rollNum = rollNum
        removed = False
        for Student in self.students:
            if (Student.rollNo == self.rollNum):
                self.students.remove(Student)
                removed = True
                print(f"Student of {self.rollNum} is 'Deleted'.\n")
        if(removed == False):
            print("Error: Nothing Find To Delete!\n")
    def findStudent(self, rollNum):
        self.rollNum = rollNum
        find = False
        for Student in self.students:
            if (Student.rollNo == self.rollNum):
                find = True
                print(f"finded: ",Student, "\n")
        if(find == False):
            print(f"No Students Exist with Roll No: {self.rollNum}\n")
    def showAllStudents(self):
        count = 1
        for Student in self.students:
            print(count, ": ", Student)
            count += 1
        print()

s1 = student("Sahil", 12, 1201)
s2 = student("Raman", 12, 1202)
s3 = student("Neelam", 12, 1203)
s4 = student("Archana", 12, 1204)

# Making School Object
School = school()

# Adding Students in School Obj
School.add(s1)
School.add(s2)
School.add(s3)
School.add(s4)


School.showAllStudents()
School.findStudent(1204)
School.removeStudent(1203)
School.showAllStudents()
School.removeStudent(1928)
