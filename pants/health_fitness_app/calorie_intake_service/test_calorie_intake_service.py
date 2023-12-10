import pytest
from unittest.mock import patch
from health_fitness_app.calorie_intake_service.calorie_intake_service import (
    cal_calories,
)


@pytest.fixture
def mock_calculate_bmr():
    with patch(
        "health_fitness_app.packages.bmr.bmr_calculator.calculate_bmr"
    ) as mock_calc_bmr:
        yield mock_calc_bmr


@pytest.fixture
def mock_calculate_calorie_intake():
    with patch(
        "health_fitness_app.packages.calorie.calorie_calculator.calculate_calorie_intake"
    ) as mock_calc_calories:
        yield mock_calc_calories


def test_cal_calories(mock_calculate_bmr, mock_calculate_calorie_intake):
    weight = 80
    height = 72
    age = 27
    sex = "male"
    activity_level = "lightly active"

    # Mock the return values of calculate_bmr and calculate_calorie_intake
    mock_calculate_bmr.return_value = 1315
    mock_calculate_calorie_intake.return_value = 1808

    result = cal_calories(weight, height, age, sex, activity_level)

    expected_result = {"daily_calorie_intake": 1808}
    assert result == expected_result
