import cv2
import os

image_folder = 'tmp'
video_name = 'tmp/video.avi'

name_list = [img for img in os.listdir(image_folder) if img.endswith('.jpg')]
full_list = [os.path.join(image_folder, i) for i in name_list]
time_sorted_list = sorted(full_list, key=os.path.getmtime)
images = [os.path.basename(i) for i in time_sorted_list]

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 10, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()