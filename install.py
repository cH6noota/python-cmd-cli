import os
from os.path import expanduser
import shutil

home = expanduser("~")

# .zshrcにpycmdのパス追加
with open(home+"/.zshrc", mode='a') as f:
    path_str = 'export PATH="$HOME/.pycmd-scripts:$PATH"'
    f.write("# Python Custom Command File\n"+path_str+"\n")

# script保存用のフォルダを作成
if os.path.exists(home+"/.pycmd-scripts")==False:
    os.mkdir(home+"/.pycmd-scripts")    

# pycmd追加
shutil.copyfile("pycmd", home+"/pycmd")
os.chmod(home+"/pycmd", 0o755)
