from setuptools import setup
from setuptools import find_packages

setup(
    # See https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html
    # for further details on the setup configuration.
    name='peritus-utils',
    version='0.1.0',
    description='Python package of my custom utils',
    url='',                  # Reference URL
    author='Alfred Iacovella',
    author_email='java.peritus@gmail.com',
    license='BSD 2-clause',
    # packages=['s3'],         # Each package will be under its own directory name.
    packages=find_packages(
        where='.',
        include=['pkg*'],
        exclude=['additional'],
    ),
    package_dir={"": "."},


    # Required depenedencies ex:  install_requires=['numpy']

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)