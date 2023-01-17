import os
import shutil

img_path = 'C:/Users/batuh/Downloads/Compressed/Mapillary-Train0/images/'

anno_path = 'C:/Users/batuh/Downloads/Compressed/Mapillary-Annotation/mtsd_v2_fully_annotated/annotations/'

dest_anno = 'C:/Users/batuh/Downloads/Compressed/train and anno/anno/'

dest_img = 'C:/Users/batuh/Downloads/Compressed/train and anno/train/'

videos = os.listdir(img_path)
annotations = os.listdir(anno_path)

for video in videos:
    img_arr = video.split('.')

    for anno in annotations:
        anno_arr = anno.split('.')

        if (img_arr[0] == anno_arr[0]):
            shutil.move(anno_path + anno, dest_anno)
            shutil.move(img_path + video, dest_img)