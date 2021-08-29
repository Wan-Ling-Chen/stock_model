import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stock-model",
    version="0.0.1",
    author="Lyn Chen",
    author_email="lynchen0103@gmail.com",
    description="Schema ORM for Stock Database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wan-Ling-Chen/stock_model.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>3.6',
    install_requires=[
        'sqlalchemy==1.4.23'
    ],
    include_package_data=True,
    packages=setuptools.find_packages()
)