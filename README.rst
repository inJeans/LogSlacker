LogSlacker
----------

A loghandler for integration with slack.

.. image:: https://badge.fury.io/py/logslacker.svg
    :target: https://badge.fury.io/py/logslacker

To use (with caution), simply do::

    >>> from logslacker import SlackLogHandler
    >>> handler = SlackLogHandler()
    >>> print handler.test()