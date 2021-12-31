# OpenCv Code  is connected to the graphics and the bassics of calculator. Will be written once the other two parts are
# done to some extent.

import cv2
from cvzone.HandTrackingModule import HandDetector
from tkinter import *

#Webcam
cap = cv2.VideoCapture(0)       # you can define the size as well. Defaul# t is 640 x 480

#HandDetection
detector = HandDetector(detectionCon=0.8, maxHands=1)       # DetectionCon is how much sure is the program that the object is a hand. value is set to 80%.


#Function to open the camera
def openCamera():
    while True:
        #Get image from the camera
        success, image = cap.read()

        #Flipping the image
        image = cv2.flip(image, 1)          # 1 will flip the image horizontally(x axis) and 0 will flip vertically (y-axis)

        #Detection of Hand
        hands, image =detector.findHands(image, flipType= False)        # Flip Type is set ot false because we have already set a flip once to not get confused in the mirror imaging of the picture.

        #Display Image
        cv2.imshow("Image", image)
        cv2.waitKey(1)          # 1 milisecond delay

print(openCamera())

# function to perform
def perform(num):
    global val
    val = val+str(num)
    data.set(val)

# function to clear
def clear():
    global val
    val = " "
    data.set(" ")

# function for equal
def equal():
    global val
    result = str(eval(val))
    data.set(result)

# display
root = Tk()
root.title("My Calculator")
root.geometry("361x381+500+200")
val = " "
data = StringVar()
display = Entry(root, textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel", 20))
display. grid(row=0, columnspan=4)
# lambda function to pass arguments
# first row
btn7 = Button(root, text="7", font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(7))
btn7.grid(row=1, column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform('+'))
btn_add.grid(row=1,column=3)

# second row
btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform('-'))
btn_sub.grid(row=2,column=3)

# third row
btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(3))
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform('*'))
btn_mul.grid(row=3,column=3)

# third row
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform(0))
btn0.grid(row=4,column=0)
btnc=Button(root,text="c",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :clear('c'))
btnc.grid(row=4,column=1)
btn_equal=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :equal('='))
btn_equal.grid(row=4,column=2)
btn_div=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :perform('/'))
btn_div.grid(row=4,column=3)
root.mainloop()



