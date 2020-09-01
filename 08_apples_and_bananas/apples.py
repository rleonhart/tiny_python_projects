#!/usr/bin/env python3
"""
Author : robert <robert@localhost>
Date   : 2020-09-01
Purpose: Apples and bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file'
                        )

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()
    # Input can be string or filename
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    new_text = []

    for char in text:
        if char in 'aeiou':
            new_text.append(vowel)
        elif char in 'AEIOU':
            new_text.append(vowel.upper())
        else:
            new_text.append(char)

    # Interesting other methods:
    # Method 2  text = text.replace(v, vowel).replace(v.upper(), vowel.upper())
    #
    # Method 3  trans = str.maketrans('aeiouAEIOU', vowel * 5 + vowel.upper() * 5)
    #           text = args.text.translate(trans)
    # Method 4  text = [vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    #           for c in args.text]
    # Method 6  text = map(lambda c: vowel if c in 'aeiou' else vowel.upper()
    #           if c in 'AEIOU' else c, args.text)
    # Method 8  text = re.sub('[aeiou]', vowel, text)
    #           text = re.sub('[AEIOU]', vowel.upper(), text)

    print(''.join(new_text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
