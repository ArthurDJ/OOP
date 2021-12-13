class Student:
    def __init__(self, firstname="Xiao", lastname="Ming", course="CS"):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.module_list = []

    def showDetails(self):
        print("Firstname is " + self.firstname + " Lastname is " + self.lastname, end='\n')
        print("Course is " + self.course, end='\n')
        if len(self.module_list) == 0:
            print('Not enrolled on any modules at this time')
        else:
            print('Enrolled on following modules:')
            for i in self.module_list:
                print(i)

    def changeCourse(self, new_course):
        self.course = new_course


class Module:
    def __init__(self, name="OOP", code="000001", tutor="Ms.Zhou"):
        self.name = name
        self.code = code
        self.tutor = tutor
        self.students_list = []

    def enrolStudent(self, student):
        self.students_list.append(student)
        student.module_list.append(self.code)

    def showAllEnrolledStudents(self):
        if len(self.students_list) == 0:
            print('No students for ', self.code, ' yet')
        else:
            print('Enrolled on module: ', self.code)
            for i in self.students_list:
                print(i.firstname + " " + i.lastname)


def main():
    # Create some students and some modules ...
    s1 = Student('a', '1', 'Math')
    s2 = Student('b', '2', 'Chinese')
    s3 = Student('c', '3', 'English')

    m1 = Module('M1', '000002', 'T1')
    m2 = Module('M2', '000003', 'T2')
    m3 = Module('M3', '000006', 'T3')

    m1.enrolStudent(s1)
    m1.enrolStudent(s2)
    m2.enrolStudent(s1)
    m2.enrolStudent(s3)

    s1.showDetails()
    s2.showDetails()
    s3.showDetails()

    m1.showAllEnrolledStudents()
    m2.showAllEnrolledStudents()
    m3.showAllEnrolledStudents()

    s1.changeCourse('engineering')
    s1.showDetails()


if __name__ == "__main__":
    main()
