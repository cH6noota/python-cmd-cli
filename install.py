#!/usr/bin/env python
import os
from os.path import expanduser
import re
import shutil

home = expanduser("~")
script_path = home + os.sep + ".pycmd-scripts"

if os.name == 'posix':
    # .zshrcにpycmdのパス追加
    with open(home+"/.zshrc", mode='a') as f:
        path_str = 'export PATH="$HOME/.pycmd-scripts:$PATH"\nexport PATH="$HOME:$PATH"'
        f.write("# Python Custom Command File\n"+path_str+"\n")

    # script保存用のフォルダを作成
    if os.path.exists(home+"/.pycmd-scripts")==False:
        os.mkdir(home+"/.pycmd-scripts")    

    # pycmd追加
    shutil.copyfile("pycmd", home+"/pycmd")
    os.chmod(home+"/pycmd", 0o755)
else:
    # script保存用のフォルダを作成
    if os.path.exists(script_path)==False:
        os.mkdir(script_path)    
        # pycmdのパス追加
        os.environ['PATH'] = script_path + ";" + os.environ['PATH']

    # pycmd追加
    application_path = home
    pathlist = os.environ.get('PATH').split(";")
    for path in pathlist:
        pattern = re.compile(r'.*Python.*' +  os.sep + 'Scripts')
        match = pattern.search(path)
        if match:
            application_path = match.group()
            break
    shutil.copyfile("pycmd", application_path + os.sep + "pycmd")
    shutil.copyfile("pycmd.bat", application_path + os.sep + "pycmd.bat")
print('install pycmd Script dir ==>' + script_path)    
print('install pycmd dir ==>' + application_path)    
print('install complete')
