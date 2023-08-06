import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='gauss-rank-scaler',                           # should match the package folder
    packages=['gauss-rank-scaler'],                     # should match the package folder
    version='0.0.3',                                # important for updates
    license='BSD',                                  # should match your chosen license
    description='A scikit-learn style transformer that scales numeric variables to normal distributions',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='aldente0630',
    author_email='aldente0630@gmail.com',
    url='https://github.com/aldente0630/gauss-rank-scaler.git', 
    install_requires=['numpy', 'joblib', 'scipy', 'scikit-learn'],  # list all packages that your package uses
    keywords=["pypi", "rank scaler", "guassian rank", "guassian rank scaler"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/ExtinctionEvent/grs/archive/refs/tags/0.0.2.tar.gz",
)