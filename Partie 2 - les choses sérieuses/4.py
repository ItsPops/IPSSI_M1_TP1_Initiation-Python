import sys
import argparse
parser = argparse.ArgumentParser(
    prog = 'Exercice 4',
    description = 'Exercice 4 des révisions Python',
    epilog = 'Francois Brille')
parser.add_argument('-f', '--file')
parser.add_argument('-c', '--create')
parser.add_argument('-r', '--rename')
parser.add_argument('-l', '--list')
parser.add_argument('-m', '--move')
parser.add_argument('-d', '--delete')
parser.add_argument('-hs', '--hash')
parser.add_argument('-h', '--help')
args = parser.parse_args()

file 


