# Refernce:  
# https://stackoverflow.com/questions/27035672/cv-extract-differences-between-two-images

import cv2
from skimage.metrics import structural_similarity as ssim

vidcap = cv2.VideoCapture('2021072113595965.mp4')
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
       cv2.imwrite("p_frame%d.png" % count, curr_frame)
       prev_frame = curr_frame
   else:
        print("Image similarity:", score)
   count += 1  