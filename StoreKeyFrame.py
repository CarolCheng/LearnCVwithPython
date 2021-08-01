# Refernce:  
# https://stackoverflow.com/questions/27035672/cv-extract-differences-between-two-images

import cv2
from skimage.metrics import structural_similarity as ssim
import sys
import os

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = 'demo'
print ('Hello', filename)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# directory = 'test'
os.mkdir(filename)
print("Directory '% s' created" % filename)

vidcap = cv2.VideoCapture(filename + ".mp4")
success,image = vidcap.read()
score_thresh = 0.95 # You may need to adjust this threshold
count = 0

# Read the first frame.
success, prev_frame = vidcap.read()
while success:
   success,curr_frame = vidcap.read()
   if success == False:
       break;
   # Convert images to grayscale
   pre_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
   curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
   # Compute SSIM between two images
   (score, diff) = ssim(pre_gray, curr_gray, full=True)
   if score < score_thresh: 
       cv2.imwrite(filename + "/" + filename + "_frame_%d.png" % count, curr_frame)
       prev_frame = curr_frame
   else:
        print("Image similarity:", score)
   count += 1  