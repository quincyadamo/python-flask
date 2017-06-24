#Write a function that generates ten scores between 60 and 100.
#Each time a score is generated, your function should display what the grade is for a particular score

def gradeScore():
	for count in range(0,11):
		from random import randint
		score = randint(60,100)

		if 60 <= score <= 69:
			print "Score:", score , "; Your grade is D"
		elif 70 <= score <= 79:
			print "Score:", score , "; Your grade is C"
		elif 80 <= score <= 89:
			print "Score:", score , "; Your grade is B"
		elif 90 <= score <= 100:
			print "Score:", score , "; Your grade is A"
		elif score > 100:
			print "You're an ROCKSTAR!"
		else:
			print "You failed. Try again next year!"

gradeScore()
