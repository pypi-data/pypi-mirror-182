from setuptools import setup, find_packages


setup(
    name='mango-explorer-v4',
    version='0.1',
    license='MIT',
    author="Mango Markets",
    author_email='support@mango.markets',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/blockworks-foundation/mango-explorer-v4'
)