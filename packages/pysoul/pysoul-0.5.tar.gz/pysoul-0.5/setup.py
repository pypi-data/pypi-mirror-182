from setuptools import setup, find_packages
setup(
    name='pysoul',
    version='0.5',
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
            'pysoul = __init__:hello'
        ]
    },

)