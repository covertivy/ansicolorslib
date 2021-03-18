from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='ansicolorslib',
    version='1.0.1',
    description='A small library containing ansi color functions.',
    author='Raz Kissos',
    author_email='kissosrazz@gmail.com',
    url='https://github.com/RazKissos/ansicolorslib',
    project_urls = {'github':'https://github.com/RazKissos/ansicolorslib'},
    packages=['ansicolorslib'],
    package_dir={'ansicolorslib': 'src/ansicolorslib'},
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    classifiers =[ 'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
)