from setuptools import setup, find_packages

with open("README.md", "r") as fh:

    long_description = fh.read()


setup(
    name='spider-web',
    version='0.0.4',
    packages=find_packages(include=["spider_web","spider_web/utils"]),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'spider-web = spider_web.record_netstat:record_netstat',
        ],
    },
    author="Julian M. Kleber",
    author_email="julian.kleber@sail.black",
    description="CLI for catching bugs on a computer system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://codeberg.org/cap_jmk/spider-web.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
