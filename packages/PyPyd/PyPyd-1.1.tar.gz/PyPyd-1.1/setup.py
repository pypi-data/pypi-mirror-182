from setuptools import setup


setup(
    name='PyPyd',
    version='1.1',
    requires=["Cython"],
    scripts=["pypyd.py"],
    url='',
    license='',
    author='Lemon',
    author_email='',
    description='Py to pyd tool',
    long_description="""
    to build a pyd file, you can use
    python -m pypyd <file> [-d|--dir <build dir>]
    use 'python -m pypyd -h' to get help
    """
)
