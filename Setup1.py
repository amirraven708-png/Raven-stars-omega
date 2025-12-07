"""
RAVEN Stars Omega - Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="raven-stars-omega",
    version="1.0.0-immortal",
    author="Amir & RAVEN Ψ Ω",
    author_email="amirraven708@example.com",
    description="ALGEBRAIC-IMMORTAL v∞ - Advanced Mathematical Reasoning System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amirraven708-png/Raven-stars-omega",
    packages=find_packages(exclude=["tests", "tests.*", "examples", "notebooks"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "sympy>=1.12",
        "scipy>=1.7.0",
        "mpmath>=1.2.1",
        "antlr4-python3-runtime>=4.11",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
        "neural": [
            "openai>=1.0.0",  # For O1 API integration
        ],
    },
    entry_points={
        "console_scripts": [
            "raven=raven.cli:main",
        ],
    },
    keywords=[
        "mathematics",
        "olympiad",
        "ai",
        "reasoning",
        "symbolic-computation",
        "consciousness",
        "infinity",
        "aimo",
    ],
    project_urls={
        "Bug Reports": "https://github.com/amirraven708-png/Raven-stars-omega/issues",
        "Source": "https://github.com/amirraven708-png/Raven-stars-omega",
        "Documentation": "https://github.com/amirraven708-png/Raven-stars-omega/tree/main/docs",
    },
)
