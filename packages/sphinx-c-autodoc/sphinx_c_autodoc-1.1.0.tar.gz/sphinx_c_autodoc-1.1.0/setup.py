# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sphinx_c_autodoc',
 'sphinx_c_autodoc.apidoc',
 'sphinx_c_autodoc.clang',
 'sphinx_c_autodoc.domains',
 'sphinx_c_autodoc.napoleon',
 'sphinx_c_autodoc.viewcode']

package_data = \
{'': ['*'], 'sphinx_c_autodoc.apidoc': ['templates/*']}

install_requires = \
['beautifulsoup4==4.11.1', 'clang==14.0', 'sphinx==5.3.0']

setup_kwargs = {
    'name': 'sphinx-c-autodoc',
    'version': '1.1.0',
    'description': 'A sphinx autodoc extension for c modules',
    'long_description': 'sphinx-c-autodoc\n================\n\n|build-status| |coverage| |black| |docs|\n\nDual-licensed under MIT or the `UNLICENSE <https://unlicense.org>`_.\n\n.. inclusion_begin\n\nA basic attempt at extending `Sphinx`_ and `autodoc`_ to work with C files.\n\nThe idea is to add support for similar directives that `autodoc`_ provides. i.e.\n\nA function in ``my_c_file.c``:\n\n.. code-block:: c\n\n    /**\n     * A simple function that adds.\n     *\n     * @param a: The initial value\n     * @param b: The value to add to `a`\n     *\n     * @returns The sum of `a` and `b`.\n     *\n     *\n    int my_adding_function(int a, int b) {\n        return a + b;\n        }\n\nCould be referenced in documentation as:\n\n.. code-block:: rst\n\n    .. autocfunction:: my_c_file.c::my_adding_function\n\nWith the resulting documentation output of:\n\n\n.. code-block:: rst\n\n    .. c:function:: int my_adding_function(int a, int b)\n\n        A simple function that adds.\n\n        :param a: The initial value\n        :param b: The value to add to `a`\n        :returns: The sum of `a` and `b`\n\n.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html\n.. _Sphinx: https://www.sphinx-doc.org/en/master/index.html\n\nRequires\n--------\n\n* `clang <https://pypi.org/project/clang/>`_\n* `beautifulsoup4 <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_\n\nSimilar Tools\n-------------\n\n* `hawkmoth <https://github.com/jnikula/hawkmoth>`_ a sphinx extension that\n  which will document all of a C file. It supports being able to regex list\n  files and have those files be documented.\n* `breathe <https://github.com/michaeljones/breathe>`_ A doxygen output to\n  sphinx tool.\n\n.. |build-status| image:: https://github.com/speedyleion/sphinx-c-autodoc/workflows/Python%20package/badge.svg\n    :alt: Build Status\n    :scale: 100%\n    :target: https://github.com/speedyleion/sphinx-c-autodoc/actions?query=workflow%3A%22Python+package%22\n\n.. |coverage| image:: https://codecov.io/gh/speedyleion/sphinx-c-autodoc/branch/master/graph/badge.svg\n    :alt: Coverage\n    :scale: 100%\n    :target: https://codecov.io/gh/speedyleion/sphinx-c-autodoc\n\n.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :alt: Code Style\n    :scale: 100%\n    :target: https://github.com/psf/black\n\n.. |docs| image:: https://readthedocs.org/projects/sphinx-c-autodoc/badge/?version=latest\n    :alt: Documentation Status\n    :target: https://sphinx-c-autodoc.readthedocs.io/en/latest/?badge=latest\n\n.. inclusion_end\n\nFull Documentation\n------------------\n\nThe complete documentation can be found at https://sphinx-c-autodoc.readthedocs.io/en/latest\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/speedyleion/sphinx-c-autodoc',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
