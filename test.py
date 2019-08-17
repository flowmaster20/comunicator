import unittest

import simple_sha


"""
File with tests that are running every time that project is pushed to github
if you want to trigger them manualy run this file
"""


class TestComunicator(unittest.TestCase):

    def test_case(self):
        input = "dom"
        ex_output = "987fb38f30bfac4d7e336f96565768e9b6e24a2365c3c5a8109ba73c"
        msg = "sha function not working"
        self.assertEqual(simple_sha(input), ex_output, msg)


if __name__ == '__main__':
    unittest.main()
