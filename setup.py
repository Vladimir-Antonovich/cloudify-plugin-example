from setuptools import setup

setup(
    name='cloudify-plugin-example',
    version='0.0.1',
    description='Writes a file',
    packages=['example_package'],
    install_requires=[
        "cloudify-plugins-common>=4.0"
    ]
)
