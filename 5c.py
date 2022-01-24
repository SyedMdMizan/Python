#WAP in python to open and write "Hello World" into a file

f=open("sample_file.txt",'w')
f.write("Hello World")
f=open("sample_file.txt",'r')
print(f.read())
f.close()
