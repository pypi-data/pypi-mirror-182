import setuptools

requirements = [
    "SQLAlchemy==1.4.45",
    "rich==12.6.0"
]

long_description = "A command line tool to keep track of the movies you watched. Installable via pip. " \
                   "Uses SqlAlchemy. Built for Linux"

setuptools.setup(
    name="my-movie-database",
    version="0.1.1",
    author="Kumuthu Edirisinghe",
    author_email="ekumuthu@gmail.com",
    description="A command line tool to keep track of the movies you watched",
    long_description=long_description,
    url="https://github.com/kumuthu53/my-movie-database",
    project_urls={
        "Bug Tracker": "https://github.com/kumuthu53/my-movie-database/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=requirements,
    scripts=["scripts/my-movie-database"]
)
