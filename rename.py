import os
import sys


mydir =r'<your files location here>'

os.chdir(mydir)
print(os.getcwd())
COUNT = 1


def increment():
    global COUNT
    COUNT += 1


for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    if f.endswith(".ppt") or f.endswith(".docx") or f.endswith(".py") or f.endswith(".doc") or "Ion" in f_name or "mdl" in f_name or "ion" in f_name :
        pass
    else:
        f_name = "DG ID number" + str(COUNT)
        increment()
        new_name = f'{f_name} {f_ext}'
        os.rename(f, new_name)






