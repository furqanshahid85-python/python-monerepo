# package containing methods for bmr calculations


def calculate_bmr(weight, height, age, sex):
    try:
        weight = float(weight)
        height = float(height)
        age = int(age)
        sex = str(sex)
        if sex == "male":
            bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
        else:
            bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
        return int(bmr)
    except ValueError:
        return None
