import os
import glob
import shutil


def create_folder(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        print("Done Create Folder")
    return path


def add_photos_to_subfolders(leafs, subfolder, copy_folders):
    create_folder(".\\plants")
    create_folder(copy_folders[0])
    create_folder(copy_folders[1])
    create_folder(copy_folders[2])
    create_folder(copy_folders[0] + subfolder)
    create_folder(copy_folders[1] + subfolder)
    create_folder(copy_folders[2] + subfolder)

    photos = glob.glob(leafs + "\\*")
    for i in range(len(photos)):
        photo = photos[i]
        photo_name = photo[photo.rfind("\\") + 1:]

        if i <= 0.7 * len(photos):
            copy_folder = copy_folders[2]  # train
        elif i <= 0.9 * len(photos):
            copy_folder = copy_folders[0]  # valid
        else:
            copy_folder = copy_folders[1]  # test

        shutil.copyfile(photo, copy_folder + subfolder + photo_name)

    print(f"Done Arranging!")


if __name__ == "__main__":
    all = glob.glob(".\\PlantVillage\\*")
    healthy = [".\\PlantVillage\\Pepper__bell___healthy", ".\\PlantVillage\\Potato___healthy",
               ".\\PlantVillage\\Tomato_healthy"]

    copy_folders = [".\\plants\\valid\\", ".\\plants\\test\\", ".\\plants\\train\\"]

    for leafs in all:
        if leafs in healthy:
            subfolder = "healthy\\"
        else:
            subfolder = "sick\\"

        add_photos_to_subfolders(leafs, subfolder, copy_folders)