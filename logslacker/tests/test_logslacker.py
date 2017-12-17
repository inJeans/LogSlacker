from unittest import TestCase

import logslacker

class TestSlacker(TestCase):
    def test_is_string(self):
        h = logslacker.SlackLogHandler()
        s = h.test()
        self.assertTrue(isinstance(s, basestring))