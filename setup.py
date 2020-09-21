from setuptools import find_packages, setup

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='syntrans',
    version='0.5.0',
    description='This is a simple engine for language-indepdent document (LID, based on ideas on definitionary.com).',
    long_description=long_description,
    long_description_content_type='text/rst',
    url='https://github.com/wefindx/synsets',
    author='Mindey',
    author_email='~@mindey.com',
    license='MIT',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'typology',
    ],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'syntrans=syntrans.trans:main',
        ],
    }
)
