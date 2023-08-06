from setuptools import find_packages, setup

with open('bit_lts/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break

setup(
    name='bit_lts',
    version=version,
    description='Bitcoin made easy.',
    long_description=open('README.rst', 'r').read(),
    author='Lts',
    author_email='nail.velichko2016@yandex.ru',
    license='MIT',

    keywords=(
        'bitcoin',
        'cryptocurrency',
        'payments',
        'tools',
        'wallet',
    ),

    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),

    install_requires=('coincurve>=18.0.0', 'pycryptodome>=3.16.0', 'requests'),
    extras_require={
        'cli': ('appdirs', 'click', 'privy', 'tinydb'),
        'cache': ('lmdb',),
    },
    tests_require=['pytest', 'requests_mock'],

    packages=find_packages(),
    entry_points={
        'console_scripts': (
            'bit = bit.cli:bit',
        ),
    },
)
