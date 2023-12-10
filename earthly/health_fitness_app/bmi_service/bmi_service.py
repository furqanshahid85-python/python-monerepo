from health_fitness_app.packages.bmi.bmi_calculator import (
    calculate_bmi,
    get_bmi_category,
)


def cal_bmi(weight, height):
    """To get your bmi enter your weight(kg) and height(m)"""
    bmi = calculate_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)
    return {"bmi_value": bmi, "bmi_category": bmi_category}
