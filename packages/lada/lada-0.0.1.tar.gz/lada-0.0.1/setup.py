from setuptools import setup

setup(
    name='lada',
    version='0.0.1',
    description='Python Library for LDSBus Devices',
    author='Prabhakaran Dharmarajan',
    author_email='prabhakaran.d@brtchip.com',
    license='MIT',
    install_requires=[
        'logging',
        'coloredlogs',
        'ftd2xx'
    ],
    url='http://www.brtsys.com',
    packages=['liblds/', 'src'],
)
