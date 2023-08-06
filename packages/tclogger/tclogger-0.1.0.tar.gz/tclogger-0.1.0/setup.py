from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='tclogger',
    version='0.1.0',    
    description='Simple wrapper for Python Logger',
    url='https://github.com/benjaminwestern/tclogger',
    author='Benjamin Western',
    author_email='code@benjaminwestern.dev',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=['tclogger'],
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  
        'Natural Language :: English',
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)