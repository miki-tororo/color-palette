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


#ag.PAUSE=1




root = tk.Tk()
root.title("GUI-test")
root.geometry("400x200")

lbl1=tk.Label(text="このラベルの色がドラック＆ドロップで転記されます",bg="#aaaaaa")
lbl1.pack()
lbl1.bind("<ButtonRelease>",release_action)


root.mainloop()
