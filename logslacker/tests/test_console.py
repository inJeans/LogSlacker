from unittest import TestCase
from logslacker.command_line import main

class TestConsole(TestCase):
    def test_basic(self):
        main()
