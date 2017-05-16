import argparse
from diary import Diary

def sep():
	print(30 * '-')

def menu():
    sep()
    print("   M A I N - M E N U   ")
    sep()
    print("\t 1. Get student average score")
    print("\t 2. Get student attendance")
    print("\t 3. Get class avg score")
    print("\t 4. Find the best student")
    print("\t 5. Print classes")
    print("\t Exit - 0")

class MainMenu:
    @staticmethod
    def main_actions():
        while True:
            choosen = raw_input()

            if choosen == '1':
                diary.show_students_average_grades()
                sep()
            elif choosen == '2':
                MainMenu.choose_student_avg(diary)
            elif choosen == '3':
                diary.show_average_grades_for_classes()
            elif choosen == '4':
                student_record = diary.the_best_student()
                student = student_record['student']
                print "The best student is {} {}. And average score is {:f}".format(
                    student['name'], student['surname'], student_record['average'])
            elif choosen == '5':
                diary.print_classes()
            elif choosen == '0':
                exit(0)

    @staticmethod
    def choose_student_avg(diary):
        name = raw_input("Type name: ")
        surname = raw_input("Type surname: ")
        classes = raw_input("Type class: ")
        sep()
        attendance = diary.attendance_students(name, surname, classes)
        if attendance == -1:
            print "Student not found"
        else:
            print "Attendance for {} {} is {:f}%".format(name, surname, attendance)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_file')
    args = parser.parse_args()

    diary = Diary(args.path_to_file)
    menu()
    MainMenu.main_actions()
