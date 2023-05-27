import os
import re

import setuptools

here = os.path.realpath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "alpaca_eval", "__init__.py")) as f:
    meta_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
    if meta_match:
        version = meta_match.group(1)
    else:
        raise RuntimeError("Unable to find `__version__`.")

setuptools.setup(
    name="alpaca_eval",
    version="0.1.0",
    description="Automatic evaluation of instruction-following models by LLMs.",
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
    author='Alpaca Team',
    install_requires=[
        "datasets",
        "openai",
        "pandas",
        "tiktoken>=0.3.2",
        "fire",
    ],
    extras_require={
        "analysis": [
            "seaborn",
            "matplotlib",
        ],
        "dev": {
            "pre-commit>=3.2.0",
            "black>=23.1.0",
            "isort",
        },
    },
    python_requires=">=3.9",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "console_scripts": [
            "alpaca_eval=alpaca_eval:main",
        ],
    },
)