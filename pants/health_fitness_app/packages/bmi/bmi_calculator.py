# package containing methods for bmi calculations


def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        bmi = weight / (height**2)
        return int(bmi)
    except ValueError:
        return None


def get_bmi_category(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
