def life_in_weeks():
    age = input("What's your age now? ")
    age_to_int = int(age)
    if not age.isdigit:
        print("This is not your age(NUMBER)")
        return
    
    if age_to_int >= 90:
        print("You've already reached or passed 90 years")
        return

    years_remaining = 90 - age_to_int

    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12
    years_remaining_ = 90 - age_to_int
    print(f"You will have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months and {years_remaining_} years left. Good luck")

life_in_weeks()