from health_fitness_app.packages.bmr.bmr_calculator import calculate_bmr
from health_fitness_app.packages.calorie.calorie_calculator import (
    calculate_calorie_intake,
)


def cal_calories(weight, height, age, sex, activity_level):
    """To get your bmr and daily calorie intake enter your: weight(lbs),
    height(in), age(years), sex(male/female), and
    activity_level(sedentary/lightly active/moderately active/ very active)"""

    bmr = calculate_bmr(weight, height, age, sex)
    calories = calculate_calorie_intake(bmr, activity_level)

    return {"daily_calorie_intake": calories}
