from setuptools import setup, find_packages

with open("README.md", "r") as fh:

    long_description = fh.read()



setup(
    name='prettify-xml',
    version='0.4.5',
    packages=find_packages(include=["prettify_xml"]),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'prettify-xml = prettify_xml.formatter:format_xml',
        ],
    },
    author="Julian M. Kleber",
    author_email="julian.kleber@sail.black",
    description="CLI for prettifying XML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.codeberg/cap_jmk/xml-formatter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
