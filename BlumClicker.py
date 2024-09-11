import cv2
import numpy as np
import pyautogui
import time
from colorama import Fore

print(Fore.GREEN ,"This app created by iliya.",Fore.RESET)
print(Fore.RED ,"IG: iliya.shenavar",Fore.RESET)
print(Fore.BLUE ,"TELEGRAM: @ilyys",Fore.RESET)
print(" ")
def find_and_click_specific_colors(duration):
    start_time = time.time()
    pyautogui.PAUSE = 0.001 

    while time.time() - start_time < duration:
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        lower_color1 = np.array([11 - 10, 229 - 10, 81 - 10])
        upper_color1 = np.array([11 + 10, 229 + 10, 81 + 10])
        lower_color2 = np.array([36 - 10, 253 - 10, 138 - 10])
        upper_color2 = np.array([36 + 10, 253 + 10, 138 + 10])

        mask1 = cv2.inRange(screenshot, lower_color1, upper_color1)
        mask2 = cv2.inRange(screenshot, lower_color2, upper_color2)
        combined_mask = cv2.bitwise_or(mask1, mask2)

        contours, _ = cv2.findContours(combined_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 50: 
                x, y, w, h = cv2.boundingRect(contour)
                pyautogui.click(x + w // 2, y + h // 2)
                
    print("Done. you catched all of them.")
    print(" ")

while True:
    user_input = input("Input 1 to start: ")
    if user_input == "1":
        print("Clicker Started.")
        duration = 35
        find_and_click_specific_colors(duration)
      
    else:
        print("Invalid input. Please try again.")
