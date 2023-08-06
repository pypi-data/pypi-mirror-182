from setuptools import setup

setup(
    name="yamdgen",
    version="0.0.8",
    description="For generating dbt yaml and md files",
    author="Muizz Lateef",
    author_email="lateefmuizz@gmail.com",
    url="https://github.com/Muizzkolapo/yamdgenerator",
    entry_points={
        'console_scripts': [
            'yamdgen = yamdgen:generate',
        ]
    }
)