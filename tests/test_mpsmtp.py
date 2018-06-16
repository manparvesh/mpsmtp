import subprocess
import sys
import time
from unittest import TestCase


class TestMPSMTP(TestCase):
    """
        Starts a server in a thread and then makes a request.
    """

    def __init__(self, methodName='runTest'):
        super(TestMPSMTP, self).__init__()

    def runTest(self):
        # create and run server in a thread
        # server_thread = ServerThread()
        # server_thread.start()

        server_script = subprocess.Popen("./tests/server.sh", shell=True)

        time.sleep(2)

        # run script to send mail to the server
        mail_sender_script = subprocess.Popen("./tests/mail_sender.sh", shell=True)

        kill_server_script = subprocess.Popen("./tests/kill_server.sh", shell=True)

        # exit server thread
        try:
            time.sleep(2)
            server_script.kill()
            mail_sender_script.kill()
            kill_server_script.kill()

            # server_thread.join(timeout=1)
            sys.exit(0)
        except SystemExit as e:
            pass
