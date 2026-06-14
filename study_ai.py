from tkinter import *
from PIL import Image, ImageTk
import cv2
from ultralytics import YOLO
from playsound3 import playsound
import time
import random
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
popup_windows = []

sound = None
sound_playing = False

window = Tk()
window.geometry("1000x600")
window.title("study ai helper")

icon_image = Image.open("logo.png")
icon = ImageTk.PhotoImage(icon_image)
window.iconphoto(True, icon)
window.config(background="#0F0F0F")

lbl = Label(window, width=600, height=360, bg="#0F0F0F")
lbl.place(relx=0.5, rely=0.35, anchor="center")

cap = cv2.VideoCapture(0)

model = YOLO("yolo26n.pt")

def show_popups():
    
    for i in range(10):
        x = random.randint(0, 1600)
        y = random.randint(0, 800)
        popup = Toplevel(window)
        popup.title("FOCUS")
        popup.geometry(f"600x400+{x}+{y}")
        popup.config(background="#C92626")
        msg = Label(popup, text="PUT THE PHONE DOWN AND LOCK IN", font=("", 15, "bold"), bg="#C92626", fg="white")
        msg.pack(expand=True)
        popup_windows.append(popup)

def close_popups():
    for popup in popup_windows:
        popup.destroy()
    popup_windows.clear()

def video_stream():
    global sound_playing
    global afterid
    global sound
    global popup_windows
    ret, frame = cap.read()

    results = model(frame)

    phone_detected = False
    for result in results:
        for box in result.boxes:
            class_number = int(box.cls)
            class_name = model.names[class_number]
            if class_name == "cell phone":
                phone_detected = True
                x1, y1, x2, y2, = int(box.xyxy[0][0]), int(box.xyxy[0][1]), int(box.xyxy[0][2]), int(box.xyxy[0][3])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)


    if phone_detected and not sound_playing:
        sound = playsound("alarm.wav", block=False)
        sound_playing = True
        show_popups()
    elif not phone_detected and sound_playing:
        if sound is not None:
            time.sleep(1)  # brief delay to prevent sound flickering when detection is unstable
            sound.stop()
        sound_playing = False
        close_popups()
             
    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    img = Image.fromarray(cv2image)

    imgtk = ImageTk.PhotoImage(image=img)
    lbl.imgtk = imgtk

    lbl.configure(image=imgtk)

    global afterid
    afterid = lbl.after(20, video_stream)
    
afterid = None
is_active = False

def activate():
    global is_active
    global sound
    global sound_playing
    is_active = not is_active

    if is_active:
        button.config(text="DEACTIVATE AI", bg="#C92626", activebackground="#A11616")
        lbl.place(relx=0.5, rely=0.35, anchor="center")
        cap.open(0)
        video_stream()
        
    elif not is_active:
        button.config(text="ACTIVATE AI", bg="#26C926", activebackground="#16A116")
        lbl.after_cancel(afterid)
        cap.release()
        lbl.place_forget()
        if sound is not None:
            sound.stop()
        sound_playing = False

        
        

button = Button(window, text="ACTIVATE AI")
button.config(command=activate)
button.config(font=("", 50, "bold"))
button.config(bg="#26C926")
button.config(activebackground="#16A116")
button.place(relx= 0.5, rely=0.8, anchor="center")

window.mainloop()