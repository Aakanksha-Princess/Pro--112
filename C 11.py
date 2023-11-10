import os 
import shutil
source = "C:/Users/HP/Downloads/ABCD"
destination = "C:/Users/HP/OneDrive/Desktop/Aakanksha"
files = os.listdir(source)
for i in files:
    name,ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Image_Files"
        path3 = destination + '/' + "Image_Files" + '/' + i
        if os.path.exists(path2):
            print("moving") 
            shutil.move(path1, path3)   
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1, path3)   