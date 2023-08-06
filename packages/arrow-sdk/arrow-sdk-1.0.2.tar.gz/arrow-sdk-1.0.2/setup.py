from setuptools import setup

setup(
    name='arrow-sdk',
    version='1.0.2',
    author='Arrow Markets',
    py_modules=['arrow_sdk', 'utilities'],  # List the names of your modules here
    install_requires=[
        'web3',
        'eth_utils',
        'eth_account',
        'requests',
        'pytz'
    ],
)
