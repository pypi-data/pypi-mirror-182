from setuptools import setup, Extension

ext_modules = []

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bm3d",
    version='4.0.1',
    description='BM3D for correlated noise.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    author='Ymir Mäkinen',
    author_email='ymir.makinen@tuni.fi',
    packages=['bm3d'],
    python_requires='>=3.5',
    install_requires=['numpy', 'scipy', 'bm4d>=4.2.3'],
    tests_require=['pytest'],
    ext_modules=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: Free for non-commercial use',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
