# file for notes


###
# code for parsing multiple files
# You can list all files in the current directory using os.listdir:

import os
for filename in os.listdir(os.getcwd()):
   with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
      # do your stuff

# Glob

# Or you can list only some files, depending on the file pattern using the glob module:

import glob
for filename in glob.glob('*.txt'):
   with open(os.path.join(os.cwd(), filename), 'r') as f: # open in readonly mode
      # do your stuff

# It doesn't have to be the current directory you can list them in any path you want:

path = '/some/path/to/file'
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
      # do your stuff
###
