from setuptools import setup, find_packages


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

def read_file(file):
    with open(file) as f:
        return f.read()

long_description = read_file("README.md")
requirements = read_requirements("requirements.txt")

setup(
    name='pyquotes',
    version='0.1',
    author='Pradelson François',
    author_email='pradelsonfrancoiss@gmail.com',
    url='https://github.com/pradelson95/pyquotes',
    description='A Python library designed to help you manage and retrieve quotes from famous authors.',
    long_description_content_type="text/markdown",  # Actualiza a markdown si usas ese formato en README.md
    long_description=long_description,
    license="MIT license",
    packages=find_packages(exclude=["test"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    keywords='quotes, random quotes, famous quotes, author quotes, python library',
    project_urls={
        'Bug Tracker': 'https://github.com/pradelson95/pyquotes/issues',
        'Documentation': 'https://github.com/pradelson95/pyquotes/wiki',
    },
    test_suite='tests',
    tests_require=['pytest'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'pyquotes-cli=pyquotes.cli:main',  # Si tienes una CLI definida
        ],
    },
    extras_require={
        'dev': ['pytest', 'tox'],  # Para desarrollo y pruebas
        'colorama': ['colorama'],
    },
)
