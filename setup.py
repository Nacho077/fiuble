import os
from setuptools import setup, find_packages

if not os.path.exists('./build'):
    os.makedirs('./build')

setup(
    name='fiuble',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'start_console_game = scripts.console:main',
            'start_game = scripts.interface:main',
        ],
    },
    options={
        'egg_info': {
            'egg_base': './build',
        }
    }
)
