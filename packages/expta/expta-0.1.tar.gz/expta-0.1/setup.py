from setuptools import setup, find_packages
setup(
    name='expta',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Track & Analyze your expenses based on TD Bank Statement',
    url='https://github.com/sahaavi/Expense-Tracker-and-Analysis',
    author='Avi&Ricky',
    author_email='avi1023@student.ubc.ca',
    python_requires='>=3.9',
)