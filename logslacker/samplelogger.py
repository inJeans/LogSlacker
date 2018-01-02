import logging
from slackloghandler import SlackLogHandler, NoStacktraceFormatter

class ContextFilter(logging.Filter):
    """
    """

SLACK_TOKEN = 'xoxp-289274891636-289747038498-289228558673-2ed610c4e7455bf8630fc75ce61d1276'
SLACK_HANDLER = SlackLogHandler(SLACK_TOKEN)

LOGGER = logging.getLogger('debug_application')
LOGGER.addHandler(SLACK_HANDLER)

FORMATTER = NoStacktraceFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
SLACK_HANDLER.setFormatter(FORMATTER)

SLACK_HANDLER.setChannel()

SLACK_HANDLER.setLevel(logging.DEBUG)
LOGGER.setLevel(logging.DEBUG)

LOGGER.error("hello")
LOGGER.debug("hello")
LOGGER.warning("message")
LOGGER.critical("wht")
