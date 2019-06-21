#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper_long(self):
        """ Running the program with -u and changing text to uppercase """
        arg_list = ['--upper', 'hello']
        parsed = self.parser.parse_args(arg_list)
        self.assertTrue(parsed.upper)
        self.assertEqual(echo.main(arg_list), 'HELLO')

    def test_upper_short(self):
        """ Running the program with -u and changing text to uppercase """
        arg_list = ['-u', 'hello']
        parsed = self.parser.parse_args(arg_list)
        self.assertTrue(parsed.upper)
        self.assertEqual(echo.main(arg_list), 'HELLO')

    def test_lower_long(self):
        """ Running the program with -l and changing text to lowercase """
        arg_list = ['--lower', 'Hello']
        parsed = self.parser.parse_args(arg_list)
        self.assertEqual(parsed.lower, True)
        self.assertEqual(echo.main(arg_list), 'hello')

    def test_lower_short(self):
        """ Running the program with -u and changing text to uppercase """
        arg_list = ['-l', 'Hello']
        parsed = self.parser.parse_args(arg_list)
        self.assertTrue(parsed.upper)
        self.assertEqual(echo.main(arg_list), 'hello')

    def test_title_long(self):
        """ Running the program with -t and changing text to capitalize """
        arg_list = ['--title', 'hELLo']
        parsed = self.parser.parse_args(arg_list)
        print(parsed)
        self.assertTrue(parsed.title)
        self.assertEqual(echo.main(arg_list), 'Hello')
    
    def test_title_short(self):
        """ Running the program with -t and changing text to capitalize """
        arg_list = ['-t', 'hELLo']
        parsed = self.parser.parse_args(arg_list)
        print(parsed)
        self.assertTrue(parsed.title)
        self.assertEqual(echo.main(arg_list), 'Hello')

    def test_alloptions(self):
        """ Check when all options are provided """
        arg_list = ['-tul', 'hELLo']
        parsed = self.parser.parse_args(arg_list)
        self.assertEqual(parsed.title, True)
        self.assertEqual(parsed.upper, True)
        self.assertEqual(parsed.lower, True)
        self.assertEqual(echo.main(arg_list), 'Hello')


if __name__ == '__main__':
    unittest.main()
