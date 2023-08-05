# https://pythonhosted.org/an_example_pypi_project/setuptools.html
# set HOME=c:\s\telos\python
# python setup.py sdist bdist_wininst upload.bat
# pip freeze > file to list installed packages
# pip install -r requirements.txt to install

# May 2022 to upload manually: twine upload dist/aggregate-0.9*.*
# enter user name and pword (mildenhall) (py... password! not Github)

import aggregate
from setuptools import setup
from pathlib import Path

tests_require = ['unittest', 'sly']
install_requires = [
    'cycler',
    'ipykernel',
    'jinja2',
    'matplotlib',
    'numpy',
    'pandas',
    'psutil',
    'pypandoc',
    'scipy',
    'sly',
    'titlecase',
    # docs
    # 'docutils',
    # 'jupyter-sphinx',
    # 'nbsphinx',
    # 'recommonmark',
    # 'setuptools',
    # 'sphinx',
    # 'sphinx-panels',
    # 'sphinx-rtd-dark-mode',
    # 'sphinxcontrib-bibtex',
    # 'sphinx-copybutton',
    # 'sphinx-toggleprompt',
    'IPython'
]


long_description = """aggregate: a powerful aggregate distribution modeling library in Python
========================================================================

What is it?
-----------

**aggregate** is a Python package providing an expressive language and fast,
accurate computations to make working with aggregate (compound) probability
distributions easy and intuitive. It allows students and practitioners to
use realistic real-world distributions that reflect the underlying
frequency and severity generating processes. It has applications in
insurance, risk management, actuarial science, and related areas.

Documentation
-------------

https://aggregate.readthedocs.io/


Where to get it
---------------

https://github.com/mynl/aggregate


Installation
------------

::

  pip install aggregate


Dependencies
------------

See requirements.txt.

License
-------

BSD 3 licence

Contributing to aggregate
-------------------------

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome.

"""

version = aggregate.__version__

setup(name="aggregate",
      description="aggregate - working with compound probability distributions",
      long_description=long_description,
      license="""BSD""",
      version=version,
      author="Stephen J. Mildenhall",
      author_email="steve@convexrisk.com",
      maintainer="Stephen J. Mildenhall",
      maintainer_email="steve@convexrisk.com",
      packages=['aggregate'],
      package_data={'': ['*.txt', '*.rst', '*.md', 'agg/*.agg', 'examples/*.py', 'examples/*.ipynb',
                         'test/*.py']},
      tests_require=tests_require,
      install_requires=install_requires,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: BSD License',
          'Topic :: Education',
          'Topic :: Office/Business :: Financial',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Education'
      ],
      project_urls={"Documentation": 'https://aggregate.readthedocs.io/en/latest/',
                    "Source Code": "https://github.com/mynl/aggregate"}
      )
