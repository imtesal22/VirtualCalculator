import cv2
from cvzone.HandTrackingModule import HandDetector
import time

class Button:  # initialization
    def __init__(self, pos, width, height, value):
        # set the arguments for the particular instances
        self.pos = pos  # whatever the user inputs
        self.width = width
        self.height = height
        self.value = value

    def draw(self, image):  # draw on the image
        # Calculator
        # Funtion Name      (width, height),(position),(color in RGB),(completely filled
        # cv2.rectangle(image,(100, 100), (200, 200), (225, 225, 225), cv2.FILLED)
        cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225),
                      cv2.FILLED)

        # cv2.rectangle(image,(100, 100), (200, 200), (50, 50, 50), 3)        # border
        cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)

        # text on calculator  (text on button),(position + push position),(font),(scale),(color)
        # cv2.putText(image,"9",(100+20,100+50),cv2.FONT_ITALIC,2,(50, 50, 50),2)
        cv2.putText(image, self.value, (self.pos[0] + 20, self.pos[1] + 50), cv2.FONT_ITALIC, 2, (50, 50, 50), 2)

    def checkClick(self, x, y, image):
        # x1 = starting point of our box
        # x2 = x1 + width
        # x1 < x < x1 + width: If true, button is clicked
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            # Chainging the color of the button to indicate that some action is being performed
            cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255),
                          cv2.FILLED)

            cv2.rectangle(image, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)

            cv2.putText(image, self.value, (self.pos[0] + 20, self.pos[1] + 80), cv2.FONT_ITALIC, 3, (0, 0, 0), 3)

            return True
        else:
            return False


# Webcam
cap = cv2.VideoCapture(0)  # you can define the size as well. Defaul# t is 640 x 480
cap.set(3, 1280)  # Changing the width of the camera output, 3 means the third propid of the videcapture class
cap.set(4, 720)  # Changing the Height of the camera output, 4 means the 4th propid of the videocapture class

# HandDetection
detector = HandDetector(detectionCon=0.8,
                        maxHands=1)  # DetectionCon is how much sure is the program that the object is a hand. value is set to 80%.
# Change max hands value to 2 to detect both hands

buttonlistvalue = [['7', '8', '9', '*'],
                   ['4', '5', '6', '-'],
                   ['1', '2', '3', '+'],
                   ['0', '/', '.', '=']]
# creating buttons
buttonlist = []  # list for all the buttons
for x in range(4):  # 4 by 4
    for y in range(4):
        xpos = x * 100 + 800  # value of x is the value of button into the size of the button + offset
        ypos = y * 100 + 150
        # button1=Button((700,150),100,100,'5')      # (position),width,height,value
        buttonlist.append(Button((xpos, ypos), 100, 100,
                                 buttonlistvalue[y][x]))  # dynamically put values    y into x for correct positioning
       # buttonlist.append(Button)

# Variables
delayCounter = 0
myEquation = ''
delaycounter = 0
# Function to open the camera

while True:
    # Get image from the camera
    success, image = cap.read()

    # Flipping the image
    image = cv2.flip(image, 1)  # 1 will flip the image horizontally(x axis) and 0 will flip vertically (y-axis)

    # Detection of Hand
    hands, image = detector.findHands(image,
                                      flipType=False)  # Flip Type is set ot false because we have already set a flip once to not get confused in the mirror imaging of the picture.

    # draw all buttons
    cv2.rectangle(image, (800, 70), (800 + 400, 70 + 100), (225, 225, 225), cv2.FILLED)  # for the calculator body
    cv2.rectangle(image, (800, 70), (800 + 400, 70 + 100), (50, 50, 50), 3)

    for button in buttonlist:
        button.draw(image)  # image on which we want to draw

    # Check for hand
    if hands:
        lmList = hands[0]['lmList']
        # lm = landmark and this is a list with all the points of our fingers

        # Points that we need: 12 and 8 . These points are of index finger tip and middle finger tip
        # Takes only two arguments so if you need more than two arguments of distance, add the same code again and change the corresponding points
        # When the distance is very less between the index and the middle finger, we will detect it as a click.
        # When the two fingers are farther apart, we will not detect that as a click.

        length, _, image = detector.findDistance(lmList[8], lmList[12], image)
        # length, _, image = detector.findDistance(lmList[12],lmList[16],image)
        x, y = lmList[8]  # Index finger as a mouse
        if length < 50 and delayCounter == 0:
            for i, button in enumerate(buttonlist):
                if button.checkClick(x, y, image) and delayCounter == 0 :
                    myValue = buttonlistvalue[int(i % 4)][int(i / 4)]  # get correct number
                    if myValue == '=':
                        myEquation = str(eval(myEquation))              #Once all the clicks are stored in the myValue variable, it it a string as: ('4+5)
                                                                #To convert it into numerical form so that it can be solved, we use EVAl
                                                                #Sing str to conver myequation to numberical form
                    else:
                        myEquation += myValue
                    delayCounter = 1

            # to avoid multiple clicks
        if delayCounter != 0:
            delayCounter += 1
            if delayCounter > 10:
                delayCounter = 0


    # Display the Equation/Result
    cv2.putText(image, myEquation, (810, 130), cv2.FONT_ITALIC, 2, (50, 50, 50), 2)

    # Display Image
    cv2.imshow("Image", image)
    cv2.waitKey(1)  # 1 milisecond delay
    key = cv2.waitKey(1)

    if key == ord('c'):
        myEquation = ''

