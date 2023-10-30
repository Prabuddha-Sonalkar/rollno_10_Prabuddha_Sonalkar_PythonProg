import os
#to create a dirctory
#os.mkdir("E:/Aditi")
print("String format",os.getcwd())
print("Byte format",os.getcwdb())


#to rename a directory
#os.renames("file1.txt","new.txt")
#os.renames("file.txt",'E:/Aditi')

#to get current directory
print("Current Directory",os.getcwd())
os.chdir("E:/demo")

#to get thr size of dir
print(os.path.getsize("E:/Aditi"))

#to list out file in directory
print("Files in current directory",os.listdir(os.getcwd()))
print("Directory content are",os.listdir("E:/Aditi"))

#to remove the directory
os.rmdir("E:/demo1")

#dir_list=os.listdir("E:/demo1")
#if len(dir_list) =0
 #   print("Directory is empty")

#print(os.path.isdir("D:/demo1))