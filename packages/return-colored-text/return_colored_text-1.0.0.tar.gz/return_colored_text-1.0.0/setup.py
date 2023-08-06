from dotenv import load_dotenv
import setuptools
import os
import path

load_dotenv()

with open('README.md', 'r') as file:
    desc = file.read()

setuptools.setup(
    name="return_colored_text",
    version="1.0.0",
    author="Md Hasnat",
    author_email=os.getenv('EMAIL'),
    packages=[path.Path(os.getcwd())],
    description="This package is for coloring the output text.",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/m-hasnat-1201/return_colored_text.git",
    license='MIT',
    python_requires='>=3.9',
    install_requires=[]
)
