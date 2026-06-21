import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Setup
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Smoothening
prev_x, prev_y = 0, 0
smoothening = 7

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror the image
    h, w, _ = img.shape
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_img)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                lmList.append(lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1)

            # Index tip (8), Thumb tip (4)
            x1 = int(lmList[8].x * screen_width)
            y1 = int(lmList[8].y * screen_height)

            x2 = int(lmList[4].x * w)
            y2 = int(lmList[4].y * h)

            # Move cursor
            curr_x = prev_x + (x1 - prev_x) / smoothening
            curr_y = prev_y + (y1 - prev_y) / smoothening
            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Check for click
            distance = np.hypot(x2 - int(lmList[8].x * w), y2 - int(lmList[8].y * h))
            if distance < 30:
                pyautogui.click()
                time.sleep(0.2)  # Debounce delay

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# %%
%pip install mediapipe==0.10.14


