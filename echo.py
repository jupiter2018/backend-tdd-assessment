#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""An enhanced version of the 'echo' cmd line utility"""
import sys
import argparse
__author__ = "jupiter2018"


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument(
        'text', help='text to be manipulated')

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    namespace = parser.parse_args(args)
    print(namespace)
    curtext = namespace.text
    if namespace.upper:
        curtext = curtext.upper()
    if namespace.lower:
        curtext = curtext.lower()
    if namespace.title:
        curtext = curtext.title()
    return curtext


if __name__ == '__main__':
    text = main(sys.argv[1:])
    print text
