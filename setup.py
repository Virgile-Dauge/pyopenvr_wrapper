from setuptools import setup, find_packages

# with open('README.md', 'r') as fh:
#     long_description = fh.read()

setup(
    name='openvrwrapper',
    packages=find_packages(exclude=["examples/*"]),
    version='0.1.0',
    description='PyOpenvr Library conveniance wrapper',
    author='Virgile Daugé',
    author_email='virgile.dauge@pm.me',
    url='https://github.com/virgileTN/pyopenvr_wrapper',
    # download_url='',
    keywords=['vive', 'tracking'],
    install_requires=['openvr >= 1.0.1701', 'numpy >= 1.15.4'],
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    classifiers="""
                Environment :: Unix (Linux)
                Intended Audience :: Developers
                Operating System :: POSIX :: Linux
                Programming Language :: Python :: 2.7
                Programming Language :: Python :: 3.5
                Topic :: Scientific/Engineering :: Visualization
                Development Status :: 4 - Beta
                """.splitlines(),
)
