#!/usr/bin/env python3
import argparse
import re

# Eijiro is a English-Japanese dictionary and contains 600k parallel corpus that can be used for training machine translation models.
# http://www.eijiro.jp/
# This script takes REIJI1441.TXT (converted to UTF-8) and split into English and Japanese files.
# It additionally cleans some tags like ■, 【出典】 and 〈俗〉.
# Example command: split_eijiro.py REIJI1441.UTF8.TXT en ja

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('english', type=argparse.FileType('w'))
parser.add_argument('japanese', type=argparse.FileType('w'))
args = parser.parse_args()

angle_bracket = re.compile('〈.+〉')
double_angle_bracket = re.compile('《.+》')
square_bracket = re.compile('［.+］')

for line in args.file:
    line = line.rstrip('\n')
    line = line.lstrip('■')
    english, japanese = line.split(' : ', 1)
    japanese = japanese.split('◆', 1)[0]
    japanese = angle_bracket.sub('', japanese)
    japanese = double_angle_bracket.sub('', japanese)
    japanese = square_bracket.sub('', japanese)
    japanese = japanese.lstrip('—')
    japanese_candidates = japanese.split('／')

    for japanese_candidate in japanese_candidates:
        print(english, file=args.english)
        print(japanese_candidate, file=args.japanese)
