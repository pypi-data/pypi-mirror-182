from setuptools import setup, find_packages

setup(
    name='arrow-sdk',
    version='1.0.7',
    author='Arrow Markets',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=['arrow_sdk', 'utilities', 'constants'],
    include_package_data=True,
    package_data={'my_package': ['abis/*.json']},
    install_requires=[
        'web3',
        'eth_utils',
        'eth_account',
        'requests',
        'pytz'
    ],
)
