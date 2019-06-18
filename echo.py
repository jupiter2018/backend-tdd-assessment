#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "jupiter2018"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-u' , '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l' , '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title',  help='convert text to titlecase', action='store_true')
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
        return curtext.upper()
    if namespace.lower:
        return curtext.lower()
    if namespace.title:
        return curtext.title()



if __name__ == '__main__':
    text = main(sys.argv[1:])
    print text
