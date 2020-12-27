'''It is main utility to work as interface.
files to be checked must be named file1.txt and file3.txt.
Even in they are source code name them as txt.'''

from sys import argv

script first, second = argv
'''
it will match token and dictionary.These modules are part of difflib'''

from difflib import SequenceMatcher
with open('first') as file_1,open('second') as file_2:
    file1_data = file_1.read()
    file2_data = file_2.read()
    similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    print similarity_ratio  #plagiarism detected

''' Currently ratio is fixed at 0.66 but it can be fixed to any other ratio'''

if similarity_ratio>0.66:
	print " \nDocument Plagersed !!!\n"
else :
    print  " \n It is OK. Not Plagerised."
