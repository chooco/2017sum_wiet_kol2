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
# one class, all data in dictionary,  use optaparse or avgparse, poython module module.py -h
# store data in python as json dump
# path to json dump in argument, print, show dairy

import json

class Diary:

	def __init__(self, path_to_file):
		with open('dairy.json', 'r') as dairy:
			self.diary = json.load(dairy)

	def val_student(self, name, surname):
		for person in self.dairy['students']:
			if person['name'] == name and person['surname'] == surname:
				return True
		return False

	def val_subject(self, choosen_subject):
		for person in self.dairy['students']:
			for subject in person['subjects']:
				if subject['name'] == choosen_subject:
					return True
		return False

	def attendance(self, name, surname):
		for person in self.dairy['students']:
			if person['name'] == name and person['surname'] == surname:
				return self.dairy['attendance']

	def student_average_scores(self, name, surname, choosen_subject=None):
		for person in self.dairy['students']:
			if person['name'] == name and person['surname'] == surname:
				student_average_score = 0
				for subject in person['subjects']:
					if choosen_subject is not None:
						if subject['name'] == choosen_subject:
							return sum(subject['grades'])/len(subject['grades'])
						else:
							continue
					else:
						student_average_score += sum(subject['grades'])/len(subject['grades'])
				student_average_score /= len(person['subjects'])
				return student_average_score


	def total_average(self):
		total_avg = 0
		for person in self.dairy['students']:
			class_avg = 0
			for subject in person['subjects']:
				student_avg = 0
				student_avg += sum(subject['grades']) / len(subject['grades'])
			class_avg += student_avg
			class_avg /= len(person['subjects'])
		total_avg /= len(self.dairy['students'])
		return total_avg
