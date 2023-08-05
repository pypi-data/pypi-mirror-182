from setuptools import setup


with open('README.md', 'r') as description_file:
    long_description = description_file.read()


setup(
    name='traice',
    version='0.1.0',
    description='Tiny yet useful tool for consistent model training logs generation',
    url='https://github.com/zeionara/traice',
    author='Zeio Nara',
    author_email='zeionara@gmail.com',
    packages=[
        'traice',
    ],
    install_requires=[
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)
