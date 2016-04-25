import os

def rename_files():
    file_list=os.listdir(r"PATH TO THE FILES");
    print(file_list)
    os.chdir(r"PATH TO THE FILES")
    for file_name in file_list:
        new_name=file_name.translate(None,"t")
        print("Old name: "+file_name+" New name: "+new_name)
        os.rename(file_name,new_name)
    
rename_files()
