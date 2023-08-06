from setuptools import setup


setup(
    name='salure_helpers_salesforce',
    version='0.0.2',
    description='Salesforce wrapper from Salure',
    long_description='Salesforce wrapper from Salure',
    author='D&A Salure',
    author_email='support@salureconnnect.com',
    packages=["salure_helpers.salesforce"],
    license='Salure License',
    install_requires=[
        'salure-helpers-salureconnect>=1',
        'requests>=2,<=3'
    ],
    zip_safe=False,
)