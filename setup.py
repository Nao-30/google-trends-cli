import os

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def read_requirements(filename):
    """Read requirements from a file."""
    with open(os.path.join("requirements", filename), "r", encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("-r") and not line.startswith("#")
        ]


# Get requirements from files
install_requires = read_requirements("base.txt")
api_requires = read_requirements("api.txt")
dev_requires = read_requirements("development.txt")
prod_requires = read_requirements("production.txt")
test_requires = read_requirements("testing.txt")

# Remove base requirements from other requires to avoid duplication
api_requires = [req for req in api_requires if req not in install_requires]
prod_requires = [
    req for req in prod_requires if req not in install_requires and req not in api_requires
]

# Remove base, api, and prod requirements from dev and test requires
dev_requires = [
    req
    for req in dev_requires
    if req not in install_requires and req not in api_requires and req not in prod_requires
]
test_requires = [
    req for req in test_requires if req not in install_requires and req not in api_requires
]

extras_require = {
    "dev": dev_requires,
    "api": api_requires,
    "prod": prod_requires,
    "test": test_requires,
    "all": api_requires + dev_requires + prod_requires + test_requires,
}

setup(
    name="gtrends-cli",
    version="0.3.2",
    author="Mohammed A. Al-Kebsi",
    author_email="mohammed.k@mohammed-al-kebsi.space",
    description="CLI and API tools for Google Trends data analysis and content suggestions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nao-30/google-trends-cli",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["gtrends=gtrends_cli.main:cli",
                            "gtrends-api=gtrends_api.main:start_api"],
    },
    extras_require=extras_require,
    include_package_data=True,
    zip_safe=False,
)
