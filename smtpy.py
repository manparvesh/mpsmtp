import click
import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


@click.group(invoke_without_command=True)
@click.option('-p', '--port', default=8081, help='Port to bind the server to')
@click.option('-a', '--address', default='localhost', help='Address to bind our server to')
@click.option('-cp', '--client-port', default=8081, help='SMTP client port')
@click.option('-ca', '--client-address', default='localhost', help='Client address')
def cli(port, address, client_port, client_address):
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
            # print(port, client_port, client_address)
            conn = SMTP(smtp_host, int(client_port), client_address)
            conn.set_debuglevel(True)

            conn.starttls()
            conn.ehlo_or_helo_if_needed()
            conn.login(smtp_username, smtp_password)
            conn.sendmail(sender, to, body)

            LOGGER.info(sender, to, subject, body)

            conn.quit()

        inbox.serve(address=address, port=int(port))
    else:
        # invalid address
        click.echo('Invalid address!')
        LOGGER.error('Invalid address!')


if __name__ == '__main__':
    cli()
