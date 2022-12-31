import os
import shutil

dst_path = "C:/Users/batuh/Downloads/Compressed/Dataset_4/wave/"
src_path = "C:/Users/batuh/Downloads/Compressed/nturgbd_rgb_s001/nturgb+d_rgb/"

os.chdir("C:/Users/batuh/Downloads/Compressed/")

videos = os.listdir(src_path)

for video in videos:
    if video.endswith("A023_rgb.avi"):
        shutil.move(src_path + video, dst_path)
        os.chdir("C:/Users/batuh/Downloads/Compressed/")
        print("Done")


"""
A8:sit down
A9:stand up
A10:clap
A23:wave
A61:put on headphone
A62:take off headphone
A69: thumb up
A70: thumb down
A71: make OK sign
"""