from setuptools import setup

setup(
    name="Dashboard",
    version="0.1.0",
    packages=["Dashboard"],
    include_package_data=True,
    install_requires=[
        "Flask",
        "psycopg2-binary",
        "plotly",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "run-app = Dashboard.app:main",
        ],
    },
)
