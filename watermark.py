import tkinter
import cv2 
from tkinter import filedialog
import os
from datetime import date
import moviepy.editor as mp
root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

pathlabel = tkinter.Label(root)
filename = filedialog.askopenfilename()
pathlabel.config(text=filename)


pathlabel.pack()

today = str(date.today())
print(filename)
  
cap = cv2.VideoCapture(filename) 
  
while(True): 
      
    # Capture frames in the video 
    ret, frame = cap.read() 
  
    # describe the type of font 
    # to be used. 
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # Use putText() method for 
    # inserting text on video 
    cv2.putText(frame,  
                today,  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4) 
  
    # Display the resulting frame 
    cv2.imshow('video', frame) 
  
    # creating 'q' as the quit  
    # button for the video 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# release the cap object 
cap.release() 
# close all windows 
cv2.destroyAllWindows() 