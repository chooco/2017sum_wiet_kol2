from __future__ import division
import json

def sep():
	print(30 * '-')

class Diary:

	def __init__(self, path_to_file):
		with open(path_to_file, 'r') as file:
			self.diary = json.load(file)['diary']
			self.classes = self.diary['classes']


	def print_classes(self):
		for school_class in self.classes:
			print school_class

	def show_students_average_grades(self):
		for school_class in self.classes:
			sep()
			print "Averages for students in {}".format(school_class)
			for student in self.classes[school_class]['students']:
				print " Student {} {}".format(student['surname'], student['name'])
				overall_average = self.average_score_student(student)
				print " Overall average is {:f}".format(overall_average)

	def show_average_grades_for_classes(self):
		for school_class in self.classes:
			sum_of_students_average_scores = 0
			for student in self.classes[school_class]['students']:
				overall_average = self.average_score_student(student)
				sum_of_students_average_scores += overall_average;
			average_for_class = sum_of_students_average_scores / len(self.classes[school_class]['students'])
			print "Averages score for class {} is {:f}".format(school_class, average_for_class)

	def the_best_student(self):
		highest_average_score = {'student': "none", 'average': 0}
		for school_class in self.classes:
			for student in self.classes[school_class]['students']:
				overall_average = self.average_score_student(student)
				if highest_average_score['average'] < overall_average:
					highest_average_score['student'] = student
					highest_average_score['average'] = overall_average
		return highest_average_score

	def average_score_student(self, student):
		sum_average = 0
		for subject in student['subjects']:
			scores = student['subjects'][subject]['grades']
			sum_average += sum(scores) / len(scores)
		overall_average = sum_average / len(student['subjects'])
		return overall_average

	def attendance_students(self, name, surname, school_class):
		attendance = -1
		if school_class in self.classes:
			for student in self.classes[school_class]['students']:
				if student['name'] == name and student['surname'] == surname:
					attendance = student['attendance']['present'] / (
						student['attendance']['present'] + student['attendance']['absent']) * 100
		return attendance