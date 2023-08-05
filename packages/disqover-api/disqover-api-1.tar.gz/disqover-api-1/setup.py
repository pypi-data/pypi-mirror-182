from setuptools import setup, find_packages


long_description = (
    'This is a placeholder. To get the real API library, install disqover-api from the private pip repository.'
)
packages = find_packages('src')


setup(
    name='disqover-api',
    version='1',
    author='ONTOFORCE',
    author_email='backend@ontoforce.com',
    url="https://www.ontoforce.com",
    description='Placeholder for the Python API for ONTOFORCE\'s DISQOVER',
    long_description=long_description,
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'src'},
    packages=packages,
)
