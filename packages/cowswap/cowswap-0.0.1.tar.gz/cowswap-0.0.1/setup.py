# type: ignore

from setuptools import find_packages, setup

setup(
    name='cowswap',
    packages=find_packages(),
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "no-local-version",
        "version_scheme": "python-simplified-semver",
    },
    description='Convenience package to get quotes from and place orders with cowswap',
    author='BobTheBuidler',
    author_email='bobthebuidlerdefi@gmail.com',
    url='https://github.com/BobTheBuidler/cowswap',
    license='MIT',
    install_requires=[
        "ape-safe==0.5.0",
        "eth_retry>=0.1.15",
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    package_data={
        "cowswap": ["py.typed"],
    },
)