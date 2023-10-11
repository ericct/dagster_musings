from setuptools import find_packages, setup

setup(
    name="ml_pipeline",
    packages=find_packages(exclude=["ml_pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "scikit-learn",
        "xgboost",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
