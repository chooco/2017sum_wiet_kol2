#
# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

import argparse
from diary import Diary

def menu():
    print(30 * '-')
    print("   M A I N - M E N U   ")
    print(30 * '-')
    print("\t 1. Get total average score")
    print("\t 2. Get student average score")
    print("\t 3. Get student attendance")
    print("\t Exit - Ctrl^C")

    choosen = input()

    if choosen == '1':
        print("Total avg score: {:.2f} ".format(diary.total_average()))
    elif choosen == '2':
        name = input("Enter the student name: ")
        surname = input("Enter the student surname: ")
        if not diary.val_student(name, surname):
            print("Student {} {} doesnt exist in class".format(name, surname))
            return
    choosen_subject = input ("Enter subject:")
    if choosen_subject:
        if not diary.val_subject(choosen_subject):
            print("Given subject dooesnt exist")
            return
        print ("Avg for student {} {} for subject {}: {} ".format(name,surname, choosen_subject, diary.student_average_scores()))
        return

    elif choosen =='3':
        name = input("Enter the student name: ")
        surname = input("Enter the student surname: ")
        if not diary.val_student(name, surname):
            print("Student {} {} doesnt exist in class".format(name, surname))
        else:
            print("Attendance for student {} {} is {} ".format(name, surname, diary.attendance()))
            return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_file')
    args = parser.parse_args()

    diary = Diary(args.path_to_file)
    menu()
