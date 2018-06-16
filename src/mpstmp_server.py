import logging
import smtpd

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class MPSMTPServer(smtpd.SMTPServer, object):
    """Logging-enabled SMTPServer instance with handler support."""

    def __init__(self, handler, *args, **kwargs):
        super(MPSMTPServer, self).__init__(*args, **kwargs)
        self._handler = handler

    def process_message(self, peer, mailfrom, rcpttos, data, *args, **kwargs):
        LOGGER.info('Collating message from {0}'.format(mailfrom))
        LOGGER.info(dict(to=rcpttos, sender=mailfrom, body=data))
        return self._handler(to=rcpttos, sender=mailfrom, body=data)
