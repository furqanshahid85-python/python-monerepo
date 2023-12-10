from health_fitness_app.packages.bmr.bmr_calculator import calculate_bmr


def test_calculate_bmr():
    # Test case for male
    result_male = calculate_bmr(80, 72, 27, "male")
    expected_result_male = 1315
    assert result_male == expected_result_male

    # Test case for invalid input (non-numeric weight)
    result_invalid = calculate_bmr("abc", 1.75, 30, "male")
    assert result_invalid is None
