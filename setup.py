from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt", "r") as f:
    required_packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="raven-stars-omega",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=required_packages,
    author="Amirabbas Alizadeh Saravi",
    author_email="amirraven708-png@example.com",
    description="A computational implementation of ATCA (Amir's Theory of Cognitive Architecture) and RAM-16.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amirraven708-png/Raven-stars-omega",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
