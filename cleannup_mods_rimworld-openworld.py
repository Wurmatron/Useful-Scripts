import os
import shutil


def cleanup_all_mods(folder):
    file_names = os.listdir(folder)
    for file_name in file_names:
        if os.path.isdir(folder + "/" + file_name):
            remove_extras_from_mod(folder + "/" + file_name)
        else:
            print("Not deleting file '" + folder + "/" + file_name + "'")


def remove_extras_from_mod(folder):
    file_names = os.listdir(folder)
    for file_name in file_names:
        if file_name != "About":
            try:
                to_be_deleted = folder + "/" + file_name
                if os.path.isdir(to_be_deleted):
                    shutil.rmtree(to_be_deleted)
                else:
                    os.remove(to_be_deleted)
                print("Removing -> " + to_be_deleted.encode('utf-8'))
            except Exception as ex:
                print('Failed to delete ' + file_name.encode('utf-8'))
                print(ex)


cleanup_all_mods("./mods")
