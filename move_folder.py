import shutil
import os


src_path = "C:/Users/batuh/Downloads/Compressed/nturgbd_rgb_s002/nturgb+d_rgb/"
dst_path = "C:/Users/batuh/Downloads/Compressed/Dataset_2/wave/"

videos = os.listdir(src_path)

for i in videos:

    if i.endswith('A023_rgb.avi'):
        shutil.move(src_path + i, dst_path)

print("Done !")

# A8: sit down
# A9: stand up
# A10: clapping
# A23: hand waving