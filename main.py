import tkinter  # tkinter GUI
import cv2  # 
import PIL.Image , PIL.ImageTk   # pillow Module for image processing
import threading
from functools import partial  # it is used for passing the arguments to the command functions of the button
import imutils
import time


stream = cv2.VideoCapture("Dhoni2.avi")

flag = True
SET_WIDTH = 600   # canvas size
SET_HEIGHT = 400


def play(speed):   # funtion for variable speeds of the video
    global flag
    print(f'You clicked on Play . Speed is {speed}')
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES , frame1 + speed)

    grabbed , frame = stream.read()
    if not grabbed :
        exit()
    frame = imutils.resize(frame , width = 700 , height=600)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0 , 0 , image = frame , anchor = tkinter.NW)
    if flag:
        canvas.create_text(260 , 70 , fill = "yellow" , font = "Times 30 bold" , text = "Decision Pending")
    flag = not flag




def out():  # funtions for giving the OUT image
    thread = threading.Thread(target=pending , args= ("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")



def not_out():  # funtions for the giving the NOTOUT image.
    thread = threading.Thread(target=pending , args= ("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOT OUT")



def pending(decision):
    # display of the decsion pending and the countdown with the interval of some time
    frame = cv2.cvtColor(cv2.imread("decision.png") , cv2.COLOR_BGR2RGB)  # decision pending
    frame = imutils.resize(frame , width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame , anchor = tkinter.NW)
    time.sleep(1)

    # 3
    frame = cv2.cvtColor(cv2.imread("three.png") , cv2.COLOR_BGR2RGB)  # decision pending
    frame = imutils.resize(frame , width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame , anchor = tkinter.NW)
    time.sleep(1)

    

    #2
    frame = cv2.cvtColor(cv2.imread("two.png") , cv2.COLOR_BGR2RGB)  # decision pending
    frame = imutils.resize(frame , width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame , anchor = tkinter.NW)
    time.sleep(1)

    #1
    frame = cv2.cvtColor(cv2.imread("one.png") , cv2.COLOR_BGR2RGB)  # decision pending
    frame = imutils.resize(frame , width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame , anchor = tkinter.NW)
    time.sleep(1)

    # decision 
    decisionIMG = 0
    if decision == "out":
        decisionIMG = "out.png"
    else:
        decisionIMG = "notout.png"

    frame = cv2.cvtColor(cv2.imread(decisionIMG) , cv2.COLOR_BGR2RGB)  # decision pending
    frame = imutils.resize(frame , width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame , anchor = tkinter.NW)
    

    


 





# setting up of the TKINTER window
window = tkinter.Tk()
window.title("Third Umpire Decision Review System")    # Title of the window

cv_img = cv2.cvtColor(cv2.imread("welcome2.png") , cv2.COLOR_BGR2RGB)  # Background Image (Welcome)
canvas = tkinter.Canvas(window , width = SET_WIDTH , height = SET_HEIGHT)  # canvas
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))  # image

image_on_canvas = canvas.create_image(0,0 ,anchor = tkinter.NW , image = photo)  # flashing of the Welcome image
canvas.pack()

# buttons to control PlayBack

btn = tkinter.Button(window , text = "<< PREVIOUS (fast)" , width = 50 , bd = 3 ,  pady = 5 , padx = 5, command=partial(play , -25))
btn.pack()

btn = tkinter.Button(window , text = "<< PREVIOUS (slow)" , width = 50 , bd = 3 ,  pady = 5 , padx = 5 , command=partial(play , -2))
btn.pack()

btn = tkinter.Button(window , text = "NEXT (slow) >>" , width = 50 , bd = 3 ,  pady = 5 , padx = 5 , command=partial(play , 2))
btn.pack()

btn = tkinter.Button(window , text = "NEXT (fast) >>" , width = 50 , bd = 3 ,  pady = 5 , padx = 5 , command=partial(play , 25))
btn.pack()

btn = tkinter.Button(window , text = "OUT" , width = 50 , bd = 3 ,  pady = 5 , padx = 5 , command = out)
btn.pack()

btn = tkinter.Button(window , text = "NOT OUT" , width = 50 , bd = 3 ,  pady = 5 , padx = 5 , command = not_out)
btn.pack()


window.mainloop()