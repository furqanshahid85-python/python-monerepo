from health_fitness_app.packages.bmi.bmi_calculator import (
    calculate_bmi,
    get_bmi_category,
)


def test_calculate_bmi():
    weight = 80
    height = 1.82

    result = calculate_bmi(weight, height)

    expected_result = 24
    assert result == expected_result


def test_get_bmi_category():
    assert get_bmi_category(16) == "Underweight"
    assert get_bmi_category(20) == "Normal weight"
    assert get_bmi_category(27) == "Overweight"
    assert get_bmi_category(32) == "Obese"
    assert get_bmi_category(None) == "Invalid input"
