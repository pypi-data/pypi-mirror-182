import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytelemetry-dsaouda-plug",
    version="0.2.0",
    author="Diego Saouda",
    author_email="dsaouda@gmail.com",
    description="A simple and default open telemetry log formatter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diego-plug/pytelemetry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)