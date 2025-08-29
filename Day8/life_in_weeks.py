def life_in_weeks(age):
    
    weeks = (age * 52)
    ninety = (90 * 52) 
    weeks_left = (ninety - weeks)
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(25)