#Grading_students

#!/usr/bin/python

n = int(raw_input())
for _ in range(n):
	grade = int(raw_input())
	if grade < 38:
		print grade
	else:
		if grade%5 > 2:
			print grade + (5 - grade%5)
		else:
			print grade