from setuptools import setup

setup(
    name='main',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
        'pyfiglet',
        'pyinputplus',
        'stdiomask',
        'pycryptodome',
        'python-secrets'
    ],
    entry_points='''
        [console_scripts]
        cyrine-khalil=main:main
    ''',
)