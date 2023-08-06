import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minuteman",
    version="0.1.0",
    author="stscoundrel",
    description="Represent and transform expressions of time eg. '5 minutes a day in a year in days' = 1.27 days.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stscoundrel/python-template",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
