# package containing methods for daily calorie intake calculations


def calculate_calorie_intake(bmr, activity_level):
    try:
        activity_level = str(activity_level)
        if activity_level == "sedentary":
            calories = bmr * 1.2
        elif activity_level == "lightly active":
            calories = bmr * 1.375
        elif activity_level == "moderately active":
            calories = bmr * 1.55
        else:
            calories = bmr * 1.725
        return int(calories)
    except ValueError:
        return None
