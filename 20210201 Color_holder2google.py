import pyautogui as ag
import pyperclip

import tkinter as tk
import tkinter.font as font

ColorHolder = tk.Tk()
ColorHolder.title("Color_holder")
ColorHolder.geometry("1000x750")

x0=10
y0=0
a=100                           #位置の変数a、bと初期値
b=70


color="#ffffff"                 #色指定の変数


entryList=[]
labelList=[]
delList=[]

#font
my_font = font.Font(family="游ゴシック",size=10,weight="bold")

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


#画面遷移ボタン(Sellection)の処理
def transition_button1(home):
    #test=tk.Toplevel()
    import ColorSelection
     
#画面遷移ボタン(Web)の処理
def transition_button2(home):
    test=tk.Toplevel()

       

#エンターキーを押したときに実行する処理
#       処理①ラベル3個の色をEntに入力されたカラーコードに変更する。
#       処理②プレビュー画面２つの色をEntに入力されたカラーコードに変更する。
#       処理③例外処理

#変数i:エンターキーが押されたエントリーボックスのインデックス番号

def colorChange(event):

    #event.widget=entryList[i]
    #print(i) 
    

    #エンターキーが押されたエントリーボックスを探す
    for i in range(len(labelList)):             
        if event.widget==entryList[i]:
            
            print(i)    
    
            try:
                labelList[i].config(bg= entryList[i].get())
                #canvas1.configureitem(id0,fg = entryList[i].get())
        
                #canvas1.configure(id1,fg = entryList[i+1].get())
        
            except tk.TclError:
                error=0

#カラー1色を追加するメソッド
def AddColor(color):         #カラーホルダーの生成（①ラジオボタン、②エントリーボックス、③ラベル）

 
    #ラジオボタンをつくる
    #radio =tk.Radiobutton(ColorHolder,font=my_font, value=int(len(radioList)), variable=var)    
    #radioList.append(radio)
       
    #エントリーボックス
    entry = tk.Entry(ColorHolder,font=my_font,width = 13,background = '#ffffff',foreground = '#000000')
    entry.bind("<Return>",colorChange)
    entryList.append(entry)
    entry.insert(0,color)
 
    #ラベルをつくる
    label=tk.Label(ColorHolder,width = 4,height = 2,relief = "groove",background =color)
    label.bind("<ButtonRelease>",release_action)
    labelList.append(label)

    #削除ボタンをつくる
    delBtn = tk.Button(ColorHolder, text="Delete")
    delBtn.bind("<Button>", DelBtn_click)
    delList.append(delBtn)

    Update_create()
    
def CreateHoler():
    AddColor("#ffffff")


"""
#☆②イベントの処理の設定
#    エンターキーが押されたときにラベルの色を変更

#入力されたエントリーボックスのインデックス「i」を探す
i=0 #仮に設定　event？.entryで設定する

for index in range (num):
    if entryList[i].get() != entryList[index].get():
        print(index)
        i=index
        print(entryList[i].get())
        entryList[i].bind("<Return>",colorChange)
        print("ラベルの色変更")

    else:
        print(index)
        print(entryList[index].get())
        print("変更なし")
"""



    

#削除ボタンの処理
def DelBtn_click(event):

    #エンターキーが押されたDelボタンを探す
    #delボタンが押されたところの配列のindexを取得したい
    for i in range(len(delList)):             
        if event.widget==delList[i]:
            print(i)
    
            #del radioList[i]  #delボタンが押されたところのindexを消す
            del entryList[i]  
            del labelList[i]
            del delList[i]
            Update_create()
            break    

def Update_create():

    for i in range(len(labelList)):
          
        #各位置再設定　(ラジオ、エントリー、ラベル、削除ボタン)
        #radioList[i].place(x=x0,y=b*(i+1))
        labelList[i].place(x=x0, y=y0+b*(i))
        entryList[i].place(x=x0+0.7*a, y=y0+b*(i)+15)
        delList[i].place(x=x0+a*2.7, y=y0+b*(i))


#プレビュー画面を載せるためのキャンバス画面(#canvas1の設定)
canvas1=tk.Canvas(width=500,height=300,bg="#000")          
canvas1.place(x=a*4.5, y=1.2*b)

#AddCollor部分のウェジェットを


#ホーム画面のボタン
selectionBtn = tk.Button(ColorHolder, text="Selection Color",
                       command=lambda:transition_button1(canvas1))  #セレクション画面に遷移するボタン           
selectionBtn.place(x=a*4.5, y=6.5*b)


webBtn = tk.Button(ColorHolder, text="Web Color Picker",
                       command=lambda:transition_button2(canvas1))  #Web画面に遷移するボタン
webBtn.place(x=a*4.5, y=8*b)

WebEntry = tk.Entry(width = 35)                                     #URL入力エントリーボックス
WebEntry.insert(0,"http://www.shido.info/py/tkinter2.html")         #エントリーボックスの初期値設定
WebEntry.place(x=a*4.5, y=9*b)



#カラーを追加するボタンの設定
addBtn = tk.Button(ColorHolder, text="Add Color", command=CreateHoler)           
addBtn.place(x=a*4.5, y=b*0.2)

#プレビュー画面(ホーム画面canvas1に追加する)
id0=canvas1.create_rectangle(0,0,250,300, fill="blue")
id1=canvas1.create_rectangle(250,0,500,300, fill="yellow")
id2=canvas1.create_text(250,150,text="Sample", fill= "red",
                     font=("MSゴシック", "40", "bold"))


#canvas1.itemconfigure(id0,fill = "orange")
#canvas1.itemconfigure(id1,fill = "red")


    
ColorHolder.mainloop()



 
