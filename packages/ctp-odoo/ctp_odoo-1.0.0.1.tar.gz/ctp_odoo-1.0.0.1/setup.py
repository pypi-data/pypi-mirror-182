from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ctp_odoo',
    version='1.0.0.1',
    description='Cybernetics Plus Function in Odoo',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Cybernetics Plus Co., Ltd.',
    author_email='dev@cybernetics.plus',
    url='https://www.cybernetics.plus',
    download_url='https://github.com/Cybernetics-Plus/ctp_odoo.git',
    license="MIT",
    packages=find_packages(),
    package_dir={'client': 'Client'},
    install_requires=[],
    tests_require=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)