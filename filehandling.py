
import os

try:
    myfile = open('MyData.txt', 'r')
    print(myfile.read())
    print()

    path = 'Images'
    if os.listdir(path) == []:
        print("No files found")
    else:
        print("files found are " + str(os.listdir(path)))

        for count,image_file in enumerate(os.listdir(path),1):
            src = f"{path}/{image_file}"
            dest = f"{path}/Plot {str(count)}.jpg"
            print(f"{src} >>>>> {dest}")
            os.rename(src,dest)

            #print(image_file.split("."))


except FileNotFoundError as e:
    print(e)