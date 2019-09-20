import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    print('[FIND]')
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_opener(filenames):
    print('[OPENER]')
    for filename in filenames:
        if filename.endswitch('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswitch('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')

        yield f
        f.close()

def gen_concatenate(iterators):
    print('[CONCATENATE]')
    for it in iterators:
        # yield from it
        yield it

def gen_grep(pattern, lines):
    print('[GREP]')
    pat = re.compile(pattern)

    for line in lines:
        if pat.search(line):
            yield line


lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?!)python', lines)
for line in pylines:
    print(line)

