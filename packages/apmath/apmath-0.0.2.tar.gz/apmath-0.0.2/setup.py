from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent

setup(
    name='apmath', version='0.0.2',
    author='Aleksander Paradiuk', author_email="olekparadiuk@gmail.com",
    license='MIT',
    description='Mathematical apmath for python.',
    packages=find_packages(exclude=("venv", "p1.py", "p2.py")),#, include="apmath"),
    long_description=(this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=["python_version>='3.8'"]#, "pygame"]
)

# python setup.py sdist
# py -m twine upload --repository pypi dist/*