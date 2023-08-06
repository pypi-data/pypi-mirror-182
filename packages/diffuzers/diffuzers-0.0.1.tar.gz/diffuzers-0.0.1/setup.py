from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="diffuzers",
        version="0.0.1",
        description="diffuzers",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Abhishek Thakur",
        url="https://github.com/abhishekkrthakur/diffuzers",
        packages=find_packages(),
        platforms=["linux", "unix"],
        python_requires=">=3.8",
    )
