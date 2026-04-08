def life_in_weeks():
    age = input("What's your age now? ")
    age_to_int = int(age)

    years_remaining = 90 - age_to_int

    day_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12
    print(f"You will have {day_remaining} Days, {weeks_remaining} Weeks and {months_remaining} Months. Good luck")

life_in_weeks()