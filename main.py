import cv2
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = 0

# webcam object
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# capture image
while True:
  _, image = webcam.read() # first variable not needed
  image = cv2.flip(image,1) # flipping image along y axis

  frame_height, frame_width, _ = image.shape # depth not needed

  rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  #hand process
  output = my_hands.process(rgb_image)
  hands = output.multi_hand_landmarks #collected all hands

  if hands:
    for hand in hands:
      drawing_utils.draw_landmarks(image, hand)
      # collecting fingerpoints
      landmarks = hand.landmark
      for id, landmark in enumerate(landmarks):
        x = int(landmark.x * frame_width)
        y = int(landmark.y * frame_height)
        # forefinger
        if id == 8:
          cv2.circle(img=image, center=(x,y), radius=8, color=(0,255,0), thickness=3)
          x1 = x
          y1 = y
        # thumb
        if id == 4:
          cv2.circle(img=image, center=(x,y), radius=8, color=(0,255,0), thickness=3)
          x2 = x
          y2 = y
        
    # calculating distance using formula
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5//4

    # drawing line from captured points
    cv2.line(image, (x1,y1), (x2,y2), (255,255,0), 5)

    # volume stuff
    if dist > 50:
      pyautogui.press("volumeup")
    else:
      pyautogui.press("volumedown")


  cv2.imshow("Hand Volume Control using Python", image)

  key = cv2.waitKey(10) #10ms

  if key == 27: # Esc
    break

webcam.release()
cv2.destroyAllWindows()
