import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="sentiment",
    version="0.1.1",
    description="python cli program to analyze sentiment in text",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BanasiakB/sentiment",
    author="BanasiakB",
    author_email="b.banasiak2000@icloud.com",
    license="MIT",
    entry_points={
        'console_scripts': [
            'sentiment = sentiment.__main__:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["sentiment"],
    include_package_data=True,
    install_requires=requirements,
)
