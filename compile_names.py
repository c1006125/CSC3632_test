import os

dir_list = os.listdir()
file = open("compile.md", "w")
file.write(dir_list)
file.close()
