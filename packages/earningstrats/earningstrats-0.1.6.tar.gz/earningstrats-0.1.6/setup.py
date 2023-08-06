from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='earningstrats',
    version = "0.1.6",
    description ='Use Stock Earnings Data to formulate strategies',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/woojuyim/earningstrats',
    # download_url = 'https://github.com/woojuyim/earningstrats/archive/refs/tags/v0.1.1.tar.gz',
    author='Wooju Yim',
    author_email='woojuyim126@gmail.com',
    license='Apache License',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',


        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    platforms=['any'],
    keywords='pandas, yahoo finance, earnings, gamma, options',
    packages = find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=['numpy', 'pandas>=1.4.2', 'scipy>=1.8.1',
                      'yahoo_fin>=0.8.9.1', 'yfinance>=0.1.70'],
    entry_points={
        'console_scripts': [
            'sample = sample:main',
        ],
    },
    include_package_data=True,

)