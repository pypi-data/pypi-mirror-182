import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="surpyval",
    # Have you updated the __version__ parameter?!?!
    version="0.10.10",
    author="Derryn Knife",
    author_email="derryn@reliafy.com",
    description="A python package for survival analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/derrynknife/SurPyval",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['autograd', 'numpy', 'scipy', 'pandas','autograd_gamma',
                      'matplotlib', 'numpy_indexed', 'numba', 'formulaic'],
    include_package_data=True,
    package_data={'': ['datasets/*.csv']},
)