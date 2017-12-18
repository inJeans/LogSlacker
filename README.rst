LogSlacker
----------

A loghandler for integration with slack.

.. image:: https://badge.fury.io/py/logslacker.svg
    :target: https://badge.fury.io/py/logslacker
.. image:: https://travis-ci.org/inJeans/LogSlacker.svg?branch=master
    :target: https://travis-ci.org/inJeans/LogSlacker
.. image:: https://img.shields.io/codecov/c/github/codecov/example-python.svg
    :target: https://codecov.io/gh/inJeans/LogSlacker
.. image:: https://readthedocs.org/projects/logslacker/badge/?version=latest
    :target: http://logslacker.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

To use (with caution), simply do::

    >>> from logslacker import SlackLogHandler
    >>> handler = SlackLogHandler()
    >>> print handler.test()