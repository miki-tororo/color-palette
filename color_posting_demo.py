import tkinter as tk
import pyautogui as ag
import pyperclip

#click and paste
def click_paste():
    #get mouse position
    x,y=ag.position()
    #click
    ag.click(x,y,clicks=1)
    #paste
    ag.keyDown("ctrl")
    ag.typewrite("v")
    ag.keyUp("ctrl")



def release_action(event):
    #to clipboard
    pyperclip.copy(event.widget["bg"])
    click_paste()

root=tk.Tk()

root.mainloop()


#ag.PAUSE=1

