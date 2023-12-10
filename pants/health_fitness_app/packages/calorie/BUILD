python_sources(
    name="lib",
)

python_tests(
    name="tests",
)

# This target allows you to build a `.whl` bdist and a
# `.tar.gz` sdist by auto-generating
#  `setup.py`. See https://www.pantsbuild.org/docs/python-distributions.
#
# Because this target has no source code, Pants cannot infer dependencies.
# It depends on `:lib`,
#  which means it will include all the non-test Python files in this
# directory and any of
#  their dependencies.
python_distribution(
    name="dist",
    dependencies=[":lib"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="health_fitness_app.calorie.calorie_calculator",
        version="0.0.1",
        description="calorie_calculator module",
    ),
)
