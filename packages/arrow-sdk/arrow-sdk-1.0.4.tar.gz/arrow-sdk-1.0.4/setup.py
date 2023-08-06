from setuptools import setup, find_packages

setup(
    name='arrow-sdk',
    version='1.0.4',
    author='Arrow Markets',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'web3',
        'eth_utils',
        'eth_account',
        'requests',
        'pytz'
    ],
)
