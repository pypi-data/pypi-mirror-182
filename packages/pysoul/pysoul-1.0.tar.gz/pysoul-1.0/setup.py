from setuptools import setup, find_packages

def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()
      
      
setup(
    name='pysoul',
    version='1.0',
    license='MIT',
    author="Ahmad Salameh",
    author_email='ahmad.majdi96@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/ahmadmajdi96/py_sal',
    keywords='pysoul',
    install_requires=[
      ],
    entry_points={
        'console_scripts': [
            'pysoul = src.pysoul.caller:main'
        ]
    },

)