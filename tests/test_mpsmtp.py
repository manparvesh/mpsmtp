import subprocess
import sys
import threading
import time
from unittest import TestCase

from click.testing import CliRunner

from mpsmtp import cli


class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.runner = CliRunner()

    def run(self):
        """
        simply runs our server by calling `mpsmtp` command
        """
        result = self.runner.invoke(cli)


class TestMPSMTP(TestCase):
    """
        Starts a server in a thread and then makes a request.
    """

    def __init__(self, methodName='runTest'):
        super(TestMPSMTP, self).__init__()

    def runTest(self):
        # create and run server in a thread
        server_thread = ServerThread()
        server_thread.start()

        time.sleep(5)

        # run script to send mail to the server
        subprocess.call("./tests/mail_sender.sh", shell=True)

        # exit server thread
        try:
            sys.exit(0)
        except SystemExit as e:
            pass
