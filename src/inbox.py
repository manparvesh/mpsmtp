# -*- coding: utf-8 -*-

import asyncore
import smtpd
from email.parser import Parser

import click
from logbook import Logger

LOGGER = Logger(__name__)


class InboxServer(smtpd.SMTPServer, object):
    """Logging-enabled SMTPServer instance with handler support."""

    def __init__(self, handler, *args, **kwargs):
        super(InboxServer, self).__init__(*args, **kwargs)
        self._handler = handler

    def process_message(self, peer, mailfrom, rcpttos, data, *args, **kwargs):
        LOGGER.info('Collating message from {0}'.format(mailfrom))
        subject = Parser().parsestr(data.decode('utf-8'))
        LOGGER.debug(dict(to=rcpttos, sender=mailfrom, subject=subject, body=data))
        click.echo(dict(to=rcpttos, sender=mailfrom, subject=subject, body=data))
        return self._handler(to=rcpttos, sender=mailfrom, subject=subject, body=data)


class Inbox(object):
    """A simple SMTP Inbox."""

    def __init__(self, port=None, address=None):
        self.port = port
        self.address = address
        self.collator = None

    def collate(self, collator):
        """Function decorator. Used to specify inbox handler."""
        self.collator = collator
        return collator

    def serve(self, port=None, address=None):
        """Serves the SMTP server on the given port and address."""
        port = port or self.port
        address = address or self.address

        LOGGER.info('Starting SMTP server at {0}:{1}'.format(address, port))
        click.echo('Starting SMTP server at {0}:{1}'.format(address, port))

        server = InboxServer(self.collator, (address, port), None)

        try:
            asyncore.loop()
        except KeyboardInterrupt:
            click.echo('Cleaning up')
            LOGGER.info('Cleaning up')
