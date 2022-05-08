from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1.0',
    description='HW 7 clean_folder',
    author='Olexandr Samus',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author_email='olexandr.samus.2004@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
)