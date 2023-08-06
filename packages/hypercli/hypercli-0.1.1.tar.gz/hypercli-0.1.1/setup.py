import setuptools

with open("./README.md", "r") as readme:
    desc = readme.read()

setuptools.setup(
    name="hypercli",
    version="0.1.1",
    author="HYP3R00T",
    author_email="",
    description="A python based CLI tool",
    long_description=desc,
    license='MIT',
    packages=['hypercli'],
    zip_safe=False,
    install_requires=['pyfiglet',
                      'Pygments',
                      'rich',
                      'termcolor'
                      ]
)
