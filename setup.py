from setuptools import find_packages, setup

setup(
    name='MLibLogging',
    version='1.0.1.15',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-dotenv'
    ]
)
