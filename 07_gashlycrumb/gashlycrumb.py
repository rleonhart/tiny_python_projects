#!/usr/bin/env python3
"""
Author : robert <robert@localhost>
Date   : 2020-08-31
Purpose: Gashlycrumb
"""

import argparse
import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        help='Letter(s)',
                        nargs='+',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    lookup = {} #create empty dictionary
    for line in args.file:
        lookup[line[0].upper()] = line.rstrip() #fill dictionary from (default) file

    pprint.pprint(lookup) #pretty print datastructures example

    for letter in args.letter:
        if letter.upper() in lookup: #lookup index in dictionary
            print(lookup[letter.upper()]) #print associated line
        else:
            print(f'I do not know "{letter}".')



# --------------------------------------------------
if __name__ == '__main__':
    main()
