import unittest

from unittest.mock import patch
from subprocess import CompletedProcess

import testbed.parser as parser


class TestParser(unittest.TestCase):

    @patch("testbed.parser.subprocess.run")
    def test_get_testbed_instance(self, subprocess):
        output = "sample header\ninstance1\tsample info1\ninstance2\tsample info2"
        subprocess.return_value = CompletedProcess("anything", 0, output, None)

        result = parser.get_instance_name()
        self.assertEqual(result, "instance1")

        result = parser.get_instance_name(1)
        self.assertEqual(result, "instance2")
