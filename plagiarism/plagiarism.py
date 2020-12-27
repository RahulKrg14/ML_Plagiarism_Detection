'''It is main utility to work as interface.
files to be checked must be named file1.txt and file3.txt.
Even in they are source code name them as txt.'''

import re
import sys
from sys import argv

script, first, second = argv
'''
it will match token and dictionary.
file_1 = sys.argv[1]
file_2 = sys.argv[2] '''



from difflib import SequenceMatcher
with open(first) as file_1,open(second) as file_2:
    file1_data = file_1.read()
    file2_data = file_2.read()
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    print(similarity_ratio)  #plagiarism detected
if similarity_ratio>0.66:
	print(" \nDocument Plagersed !!!\n")
else :
    print(" \n It is OK. Not Plagerised.")
