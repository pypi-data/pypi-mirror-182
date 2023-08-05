import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='grew',
    version='0.5.1',
    packages=['grew',],
    license='LICENSE/Licence_CeCILL_V2-en.txt',
    description="DEPRECATED: replaced by https://pypi.org/project/grewpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://grew.fr/usage/python",
    author="bguil",
    author_email="Bruno.Guillaume@loria.fr"
)
