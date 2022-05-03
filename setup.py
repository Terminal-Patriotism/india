from setuptools import setup

setup(
    name = "india",
    version = "0.1.0",
    description = "Prints Indian flag",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/india",
    packages = ["india"],
    entry_points = {
        'console_scripts': [
            'india = india.__main__:main'
        ]
    },
)
