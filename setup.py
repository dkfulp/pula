from setuptools import setup, find_packages

long_description_text = '''
Pula is a python library that is meant to encompass the many various functions that the ordinary user
finds themselves needing in the different projects they are working on. These functions can span from 
simple is_number functions all the way to file functions such as getting all lines of text from a directory 
of code / text files.

By putting all of these functions into one library, we hope to clean up other users code and make solving 
their problems easier as well as more efficient.
'''


setup(name='pula',
      version='1.0.0.dev3',
      description='Convienent add-on library for Python, providing frequently used functions.',
      long_description= long_description_text,
      url='https://github.com/dkfulp/pula',
      author='dkfulp',
      author_email='dkfulp@coastal.edu',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      license = 'MIT',
      keywords='convenient scripting tools',
      packages=['pula'],
      #install_requires=[]
      )
