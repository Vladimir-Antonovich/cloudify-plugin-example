from setuptools import setup

setup(
    name='cloudify-plugin-example',
    version='0.0.2',
    description='Writes a file',
    packages=['example_package'],
    install_requires=[
        "cloudify-plugins-common>=5.0.5"
    ]
)
