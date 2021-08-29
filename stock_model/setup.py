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
    url="",
    
)