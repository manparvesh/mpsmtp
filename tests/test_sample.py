from unittest import TestCase

from click.testing import CliRunner

from smtpy import cli


class TestSample(TestCase):
    """
        Sample Test
    """

    def __init__(self, methodName='runTest'):
        super(TestSample, self).__init__()
        self.runner = CliRunner()

    def runTest(self):
        # run cli normally
        # result = self.runner.invoke(cli)
        # output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        # self.assertEqual(0, result.exit_code)
        # self.assertEqual("Hello, fellow Python programmer!!\n", output_string)
        pass
