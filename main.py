#A program that calculates caloric needs based on Mifflin-St Jeor equation.
import equations

def BMR_calculation():
    active = True
    while active:
        gender = equations.gender_input()
        weight = equations.weight_input()
        height = equations.height_input()
        age = equations.age_input()
        activity_level = equations.activity_input()

        equations.calculate_mifflin(gender, weight, height, age, activity_level)

        #Does the user want to continue?
        go_on = input("Do you need any other help(y/n)?: ")
        if go_on == 'n':
            active = False
        print("-------------------------------------------------------------------------------------------------")

BMR_calculation()        