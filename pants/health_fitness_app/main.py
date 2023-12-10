from health_fitness_app.bmi_service.bmi_service import cal_bmi
from health_fitness_app.calorie_intake_service.calorie_intake_service import (
    cal_calories,
)


if __name__ == "__main__":
    print(cal_bmi(weight=80, height=1.82))
    print(
        cal_calories(
            weight=80, height=72, age=27, sex="male", activity_level="lightly active"
        )
    )
