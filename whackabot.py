# https://www.classicgame.com/game/Whack+a+Mole

#imports
from re import template
import cv2
import pyautogui
from time import sleep

#No cooldown time
pyautogui.PAUSE = 0

#template and dimensions
template = cv2.imread("imgs/nose.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
template_w, template_h = template_gray.shape[::-1]

# game window dimensions
x, y, w, h = 523, 247, 875, 679

#wait
sleep(3)

#main

while True:

    #screenshot
    pyautogui.screenshot("imgs/image.png", (x, y, w, h))
    image = cv2.imread("imgs/image.png")

    while True:

        #show what the computer sees
        image_mini = cv2.resize(
            src = image,
            dsize = (450,350) #must be integer, not float
        )
        cv2.imshow("vision", image_mini)
        cv2.waitKey(10)

        image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(
            image = image_gray,
            templ = template_gray,
            method = cv2.TM_CCOEFF_NORMED
        )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        #threshold
        if max_val >= 0.8:
            #pyautogui.click(
            #    x = max_loc[0] + x, #screen x
            #    y = max_loc[1] + y  #screen y
            #)

            image = cv2.rectangle(
                img = image,
                pt1 = max_loc,
                pt2 = (
                    max_loc[0] + template_w, # = pt2 x 
                    max_loc[1] + template_h # = pt2 y
                ),
                color = (0,0,255),
                thickness = -1 #fill the rectangle
            )
        
        else:
            break