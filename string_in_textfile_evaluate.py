# read from a text file
# and append to a new file if the line contains a string

import sys
import datetime
# todays date
today = datetime.date.today()

original_file = open('robinhood_v2.txt', 'r')

new_file = open(f"output{today}.txt", 'a')


for line in original_file:
    if "robinhood" in line:
        new_file.write(line)