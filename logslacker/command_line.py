from __future__ import print_function

import logslacker

def main():
    handler = logslacker.SlackLogHandler()
    print(handler.test())
