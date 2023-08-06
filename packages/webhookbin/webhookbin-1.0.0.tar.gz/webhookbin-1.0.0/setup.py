"""
    seting up the package
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webhookbin",
    version="1.0.0",
    author="Sumiza",
    author_email="sumiza@gmail.com",
    description="Python library for webhookbin.net",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sumiza/webhookbin-library/",
    project_urls={
        "Bug Tracker": "https://github.com/Sumiza/webhookbin-library/issues",
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=['requests']
)
