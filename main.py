# pe.py
# Author:   Anhility <anhility@gmail.com>

# imports
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-n", "--name", help="your name")

args = argParser.parse_args()
print("args=%s" % args)
print("args.name=%s" % args.name)
print("Hello world!")
