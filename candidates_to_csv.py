#!/usr/bin/env python3

import string, csv

with open('candidate_dump.txt', 'r') as raw:
    candidates = []
    for line in raw.readlines():
        line = line.strip()
        if not line:
            print('Ignoring empty line')
            continue
        if any(ss in line
               for ss in ['Hottest 100', 'VOTING', 'COUNTDOWN']):
            print('Ignoring: {}'.format(line))
            continue
        if (len(line) <= 2 and line.isdigit()):
            print('Ignoring: {}'.format(line))
            continue

        if '-' in line:
            candidates.append(line)
        else:
            candidates[-1] += ' ' + line

    candidates = [[s.strip() for s in c.split('-')]
                  for c in candidates]

    with open('candidates.csv', 'w', newline='') as csv_file:
        csv.writer(csv_file).writerows(candidates)
