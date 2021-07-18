#! /usr/bin/env python
import os
import re
 
# print("join(): " + os.path.join(os.path.abspath(os.path.dirname(__file__)), "file.py"))

#print(os.path.abspath(os.path.dirname("python")))
#print(os.environ['PATH'])
#print(os.environ.get('PATH'))
pathlist = os.environ.get('PATH').split(";")
for path in pathlist:
    pattern = re.compile(r'.*Python.*' +  os.sep + 'Scripts')
    match = pattern.search(path)
    if match:
        print(match.group())
        break
