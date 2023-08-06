from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup (
    name='tokengen',
    version='0.1.1',
    author='Sharhan Alhassan',
    author_email='sharhan.alhassan@tiacloud.co',
    description='A simple CLI utility for automating token generations with kubernetes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'tokengen=tokengen.cli:main',
        ],
    }
)