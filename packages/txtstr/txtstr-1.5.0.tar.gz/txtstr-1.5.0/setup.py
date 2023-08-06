import setuptools

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()



setuptools.setup(
    name="txtstr",
    version="1.5.0",
    author="PingüiMaya",
    description="Edit text file, encrypt and decrypt with python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PinguiMaya/txtstr",
    project_urls={
        "Bug Tracker": "https://github.com/PinguiMaya/txtstr/issues",

        "Author Website" : "https://pingui.tk",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">3.8",
)