# import the necessary packages
import cv2
import numpy as np
import os

def create_pos_n_negs():    

    for file_type in ['right_dataset']:

        for img in os.listdir(file_type):
            if file_type == 'right_dataset':
                line = file_type + '/' + img + '\n'
                with open('bg.txt' , 'a') as f:
                    f.write(line)
            elif file_type == 'left_dataset':
                line = file_type + '/' + img + ' 1 0 0 100 100\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
n = 1
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
 
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        #print(refPt)
        x_diff = refPt[1][0] - refPt[0][0]
        y_diff = refPt[1][1] - refPt[0][1]
        #print(x_diff)
        #print(y_diff)
        if x_diff >= y_diff:
            y_now = refPt[1][1] + (x_diff - y_diff)
            x_now = refPt[1][0]
        elif x_diff < y_diff:
            x_now = refPt[1][0] + (y_diff - x_diff)
            y_now = refPt[1][1]
        #print(x_now)
        #print(y_now)
        refPt.append((x_now,y_now))
        cropping = False
        #print(refPt)
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 0, 255), -1)
        cv2.rectangle(image, refPt[0], refPt[2], (0, 255, 0), 2)
        cv2.imshow("image", image)
# load the image, clone it, and setup the mouse callback function


for filename in os.listdir('left_samples'):

    image = cv2.imread(os.path.join('left_samples',filename))
    image = cv2.resize(image, (0,0), fx = 0.5, fy=0.5)
    clone = image.copy()

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
     
    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
     
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone.copy()

        if key == ord("s"):
            if len(refPt) == 3:
                roi = clone[refPt[0][1]:refPt[2][1], refPt[0][0]:refPt[2][0]]
                roi = cv2.resize(roi, (100,100))
                cv2.imwrite("left_dataset/" + str(n) + '.jpg',roi)
                n = n + 1 

        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break

# for filename in os.listdir('right_samples'):

#     image = cv2.imread(os.path.join('right_samples',filename))
#     image = cv2.resize(image, (0,0), fx = 0.5, fy=0.5)
#     clone = image.copy()

#     cv2.namedWindow("image")
#     cv2.setMouseCallback("image", click_and_crop)
     
#     # keep looping until the 'q' key is pressed
#     while True:
#         # display the image and wait for a keypress
#         cv2.imshow("image", image)
#         key = cv2.waitKey(1) & 0xFF
     
#         # if the 'r' key is pressed, reset the cropping region
#         if key == ord("r"):
#             image = clone.copy()

#         if key == ord("s"):
#             if len(refPt) == 3:
#                 roi = clone[refPt[0][1]:refPt[2][1], refPt[0][0]:refPt[2][0]]
#                 roi = cv2.resize(roi, (100,100))
#                 cv2.imwrite("right_dataset/" + str(n) + '.jpg',roi)
#                 n = n + 1 

#         # if the 'c' key is pressed, break from the loop
#         elif key == ord("c"):
#             break
 
create_pos_n_negs() 
cv2.destroyAllWindows()
# 2000 positives to be trained against 1000 negatives