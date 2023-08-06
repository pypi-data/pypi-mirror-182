from setuptools import setup, find_packages


setup(
    name="lexisnexisapi",
    version='2.0.24',
    license='MIT',
    author="Robert Cuffney",
    author_email='robert.cuffney@lexisnexis.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)