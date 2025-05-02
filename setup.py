from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extras_require = {
    'dev': [
        'pytest>=6.0',
        'pytest-cov>=2.12',
        'black>=21.5b2',
        'isort>=5.9.1',
        'flake8>=3.9.2',
    ],
}

setup(
    name="gtrends",
    version="0.2.0",
    author="KitabTune",
    author_email="info@kitabtune.com",
    description="CLI tool for Google Trends data analysis and content suggestions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kitabtune/google-trends-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "trendspy>=0.1.6",
        "click>=8.1.3",
        "pandas>=1.5.0",
        "rich>=13.3.5",
        "python-dateutil>=2.8.2",
        "matplotlib>=3.5.0",
    ],
    entry_points={
        "console_scripts": [
            "gtrends=gtrends.cli:main",
        ],
    },
    extras_require=extras_require,
)
