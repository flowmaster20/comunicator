import unittest


"""
File with tests that are running every time that project is pushed to github
if you want to trigger them manualy run this file
"""


class TestComunicator(unittest.TestCase):

    def test_case(self):
        input = "dom"
        ex_output = ["d", "do", "dom"]
        msg = "should be [\"d\",\"do\",\"dom\"]"
        self.assertEqual(funkcja(input), ex_output, msg)


if __name__ == '__main__':
    unittest.main()
