import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from bugfinder import exported
setuptools.setup(
    name="texthandler",
    version="0.0.3",  # Latest version .
    author="slipper",
    author_email="r2fscg@gmail.com",
    description="ok",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/private_repo/",
    packages=setuptools.find_packages(),
    package_data={
        setuptools.find_packages()[0]: [
            "bash/*"
        ]
    },
    install_requires=['codefast', 'premium', 'fastapi', 'uvicorn', 'torch'],
    entry_points={
        'console_scripts': ['texthandle=texthandler.api:texthandle']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
