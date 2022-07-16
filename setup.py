from setuptools import setup, find_packages

setup(
    name='interactions_wait_for_plus',
    version='0.1',
    packages=["interactions.ext.wait_for_plus"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["discord-py-interactions>=4.1.0"],
)
