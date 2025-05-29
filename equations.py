import math

#Mifflin-St Jeor equations
def mifflin_male(weight, height, age):
	mifflin = math.ceil(weight*10 + height*6.25 - age*5 + 5)
	return mifflin

def mifflin_female(weight, height, age):
	mifflin = math.ceil(weight*10 + height*6.25 - age*5 - 161)
	return mifflin

def calculate_mifflin(gender, weight, height, age, activity_level):
	if gender == 'm':
		return print(f"Your basal metabolic rate (BMR) is: {mifflin_male(weight, height, age)} kcal. However, considering your activity level it is {math.ceil(mifflin_male(weight, height, age)*activity_level)} kcal.")
	elif gender == 'f':
		return print(f"Your basal metabolic rate (BMR) is: {mifflin_female(weight, height, age)} kcal. However, considering your activity level it is {math.ceil(mifflin_female(weight, height, age)*activity_level)} kcal.")

#Gender input
def gender_input():
	while True:
		gender = input("Please input your gender(M/F): ").strip().lower()

		if gender in ['m', 'f']:
			return gender
		else:
			print("ERROR! Please input 'M' or 'F' for gender.")

#Weight input
def weight_input():
	while True:
		try:
			weight = float(input("Please input your weight(kg): ").replace(',','.'))
			return weight
		except ValueError:
			print("ERROR! Please input data in correct format(numerical).")

#Height input
def height_input():
	while True:
		try:
			height = float(input("Please input your height(cm): ").replace(',','.'))
			return height
		except ValueError:
			print("ERROR! Please input data in correct format(numerical).")

#Age input
def age_input():
	while True:
		try:
			age = float(input("Please input your age: ").replace(',','.'))
			return age
		except ValueError:
			print("ERROR! Please input data in correct format(numerical).")

#Activity input
def activity_input():
	while True:
		try:
			activity_level = float(input("Please input your activity level\n\t1 - Sedentary: little or no excercise\n\t2 - Light: exercise 1-3 times/week\n\t3 - Moderate: exercise 4-5 times/week\n\t4 - Active: daily exercise or intense exercise 3-4 times/week\n\t5 - Very Active: intense exercise 6-7 times/week\n\t6 - Extra Active: intense exercise daily, or physical job: "))

			# Sprawdzenie, czy wartość mieści się w zakresie od 1 do 6
			if activity_level not in range(1, 7):
				print("ERROR! Please input a integer between 1 and 6.")
				continue

			# Przypisanie wartości współczynnika aktywności
			if activity_level == 1:
				activity_level = 1.2
			elif activity_level == 2:
				activity_level = 1.37
			elif activity_level == 3:
				activity_level = 1.46
			elif activity_level == 4:
				activity_level = 1.55
			elif activity_level == 5:
				activity_level = 1.72
			elif activity_level == 6:
				activity_level = 1.9
			return activity_level

		except ValueError:
			print("ERROR! Please input data in correct format(numerical).")

