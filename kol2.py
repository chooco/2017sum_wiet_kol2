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


class Diary:

	def __init__(self, name, surname, attendance):
		self.student = []
		self.student.append.(name + " " + surname)
        	self.student.append(attendance)

	def name(self):
		return self.student[0]

	def attendance(self):
		return self.student[1]

	def scores(self):
		return self.student[2]

	def average(self):
		average = 0
		for i in self.student[2]:
			avgerage += i
		avgerage = avgverage/len(self.student[2])
		return avgerage



