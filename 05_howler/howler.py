#!/usr/bin/env python3
"""
Author : robert <robert@localhost>
Date   : 2020-08-31
Purpose: Howler
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()
    # Input can be string or filename
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
