
import six
import json
from logging import Handler, CRITICAL, ERROR, WARNING, INFO, FATAL, DEBUG, NOTSET, Formatter
from slackclient import SlackClient, exceptions

ERROR_COLOR = 'danger'
WARNING_COLOR = 'warning'
INFO_COLOR = '#439FE0'

ERROR_CHANNEL = '#errors'
INFO_CHANNEL = '#info'
GENERAL = '#general'

CHANNEL = {
    CRITICAL: ERROR_CHANNEL,
    FATAL: ERROR_CHANNEL,
    ERROR: ERROR_CHANNEL,
    WARNING: ERROR_CHANNEL,
    INFO: INFO_CHANNEL,
    DEBUG: INFO_CHANNEL,
    NOTSET: GENERAL,
}

COLORS = {
    CRITICAL: ERROR_COLOR,
    FATAL: ERROR_COLOR,
    ERROR: ERROR_COLOR,
    WARNING: WARNING_COLOR,
    INFO: INFO_COLOR,
    DEBUG: INFO_COLOR,
    NOTSET: INFO_COLOR,
}

class NoStacktraceFormatter(Formatter):
    def formatException(self, ei):
        return None

class SlackLogHandler(Handler):

    def __init__(self, api_key, stack_trace=True, fail_silent=False):

        # initialise standard handler attributes
        Handler.__init__(self)

        # initialise custom attributes
        self.stack_trace = stack_trace
        self.client = SlackClient(api_key)
        self.channel = CHANNEL[NOTSET]

    # redo this section to be a bit nicer 
    def setChannel(channelSettings=CHANNEL):
        global CHANNEL

        if (channelSettings.__eq__(CHANNEL)):
            return None

        for level, channel in channelSettings.items():
            CHANNEL[level] = channel

    def build_msg(self, record):

        # set the output channel
        self.channel = CHANNEL.get(record.levelno, NOTSET)
        return six.text_type(self.format(record))

    def build_trace(self, record, fallback):

        trace = {
            'fallback': fallback,
            'color': COLORS.get(record.levelno, INFO_COLOR),
            'text': record.message
        }

        if record.exc_info:
            trace['text'] = '\n'.join(traceback.format_exception(*record.exc_info))

        return trace

    def emit(self, record):
        print(record)
        message = self.build_msg(record)
        if self.stack_trace:
            trace = self.build_trace(record, fallback=message)
            properties = [trace]
        else:
            properties = None

        try:

            self.client.api_call(
                "chat.postMessage",
                text = message,
                channel = self.channel,
                attachments = properties
            )

        except exceptions.SlackClientError as e:
            if self.fail_silent:
                pass
            else:
                raise e
