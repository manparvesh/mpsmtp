import logging

import click

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-p', '--port', default=8081, help='Port to bind the server to')
@click.option('-a', '--address', default='localhost', help='Address to bind our server to')
def cli(ctx, port, address):
    """
    Simple example of a click application for writing
    complex command line applications in python
    """
    if ctx.invoked_subcommand is None:
        # very basic address validation
        if address.count('.') == 3 or address == 'localhost':
            from src.mpinbox import MPInbox

            mpinbox = MPInbox()

            @mpinbox.collate
            def collate(to, sender, body):
                LOGGER.info('Received email!!!!!!!!!!!\nto:{0}\nsender:{1}\nbody:{2}'.format(to, sender, body))

            mpinbox.serve(address=address, port=int(port))
        else:
            # invalid address
            click.echo('Invalid address!')
            LOGGER.error('Invalid address!')


@cli.command()
@click.argument('address')
@click.argument('port')
def debug(address, port):
    import smtpd
    import asyncore

    LOGGER.info('Running a debug server on {0}:{1}'.format(address, port))
    server = smtpd.DebuggingServer((address, int(port)), None)

    asyncore.loop()


if __name__ == '__main__':
    cli()
