from setuptools import setup

from blockchain_exploration import VERSION

with open('README.md', 'r') as input:
    long_description = input.read()

setup(
    name='blockchain-exploration',
    version=VERSION,
    description='Exploring the blockchain with hyperlinks',
    keywords='blockchain link hyperlink sweet',
    license='MIT',
    author="Owen Miller",
    include_package_data=True,
    author_email='Owen Miller <owen@sweet.io>',
    python_requires='>=3.7',
    url='https://github.com/sweet-io-org/blockchain_exploration',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        "Operating System :: OS Independent",
    ],
    packages=['blockchain_exploration'],
    install_requires=[]
)
