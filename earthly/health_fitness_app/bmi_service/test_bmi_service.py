import pytest
from unittest.mock import patch
from health_fitness_app.bmi_service.bmi_service import cal_bmi


@pytest.fixture
def mock_calculate_bmi():
    with patch(
        "health_fitness_app.packages.bmi.bmi_calculator.calculate_bmi"
    ) as mock_calc_bmi:
        yield mock_calc_bmi


@pytest.fixture
def mock_get_bmi_category():
    with patch(
        "health_fitness_app.packages.bmi.bmi_calculator.get_bmi_category"
    ) as mock_get_category:
        yield mock_get_category


def test_cal_bmi(mock_calculate_bmi, mock_get_bmi_category):
    weight = 80
    height = 1.82

    # Mock the return values of calculate_bmi and get_bmi_category
    mock_calculate_bmi.return_value = 24
    mock_get_bmi_category.return_value = "Normal weight"

    result = cal_bmi(weight, height)

    expected_result = {"bmi_value": 24, "bmi_category": "Normal weight"}
    assert result == expected_result
