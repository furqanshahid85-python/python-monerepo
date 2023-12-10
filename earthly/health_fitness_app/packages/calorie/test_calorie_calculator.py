from health_fitness_app.packages.calorie.calorie_calculator import (
    calculate_calorie_intake,
)


def test_calculate_calorie_intake():
    # Test case for BMR of 1669.5 and sedentary activity level
    result_sedentary = calculate_calorie_intake(1669.5, "sedentary")
    assert result_sedentary == 2003

    # Test case for BMR of 1367.8 and lightly active activity level
    result_lightly_active = calculate_calorie_intake(1367.8, "lightly active")
    assert result_lightly_active == 1880

    # Test case for BMR of 1200 and moderately active activity level
    result_moderately_active = calculate_calorie_intake(1200, "moderately active")
    assert result_moderately_active == 1860

    # Test case for BMR of 1500 and very active activity level
    result_very_active = calculate_calorie_intake(1500, "very active")
    assert result_very_active == 2587
