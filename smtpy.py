import click
from logbook import Logger

LOGGER = Logger(__name__)


@click.group(invoke_without_command=True)
@click.option('-p', '--port', default=8081, help='Port to bind the server to')
@click.option('-a', '--address', default='localhost', help='Address to bind our server to')
def cli(port, address):
    """
    Simple example of a click application for writing
    complex command line applications in python
    """
    # very basic address validation
    if address.count('.') == 3 or address == 'localhost':
        from src.inbox import Inbox
        from smtplib import SMTP

        inbox = Inbox()

        smtp_host = address
        smtp_username = 'username'
        smtp_password = 'password'

        @inbox.collate
        def handle(to, sender, subject, body):
            """
            Forward a message via an authenticated SMTP connection with
            starttls.
            """
            # click.echo(sender, to, body)
            # print(port, address, body)
            conn = SMTP(smtp_host, 8081, address)

            conn.starttls()
            conn.ehlo_or_helo_if_needed()
            conn.login(smtp_username, smtp_password)
            conn.sendmail(sender, to, subject, body)

            click.echo(sender, to, subject, body)

            conn.quit()

        inbox.serve(address='localhost', port=8081)
    else:
        # invalid address
        click.echo('Invalid address!')
        LOGGER.error('Invalid address!')


if __name__ == '__main__':
    cli()
