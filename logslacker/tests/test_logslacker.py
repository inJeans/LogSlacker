from unittest import TestCase
from six import string_types

import logslacker

class TestSlacker(TestCase):
    def test_is_string(self):
        h = logslacker.SlackLogHandler()
        s = h.test()
        self.assertTrue(isinstance(s, string_types))
