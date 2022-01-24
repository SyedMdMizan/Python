#wap in python to open a file and check what are the access permission
#acquired by that file using os module

import os

read= os.access("sample_file.txt",os.R_OK)
if read:
    print("File has reading access")
else:
    print("File doesn't have reading access")

write= os.access("sample_file.txt",os.W_OK)
if write:
    print("File has writing access")
else:
    print("File doesn't have writing access")
