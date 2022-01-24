#WAP in pyhton to write the content "hi pyhton programming" for existing file
f=open("sample_file.txt",'a')
f.write("\nHi pyhton programming")
f=open("sample_file.txt",'r')
print(f.read())
f.close()
