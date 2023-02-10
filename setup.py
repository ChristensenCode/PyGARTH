from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='PyGARTH',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Automatic regression testing harness in Python.",
    license="MIT",
    author="Ryan Christensen",
    author_email='ryan.john.christensen12@gmail.com',
    url='https://github.com/ChristensenCode/PyGARTH',
    packages=['PyGARTH'],
    entry_points={
        'console_scripts': [
            'PyGARTH=PyGARTH.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='PyGARTH',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
