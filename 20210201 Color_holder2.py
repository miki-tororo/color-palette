import tkinter as tk

ColorHolder = tk.Tk()
ColorHolder.title("Color_holder")
ColorHolder.geometry("1500x750")

a=100                           #位置の変数a、bと初期値
b=50

var=tk.IntVar()                 #ラジオボタンのチェックの有無の変数var
var.set(0)                      #ラジオボタンのチェックの初期値　valure=0(一つ目)に設定

color="#ffffff"                 #色指定の変数
colorList = ['#ffffff','#000080','#ffff00']

radioList=[]
entryList=[]
labelList=[]
delList=[]
num=0



#ホーム画面の設定
canvas1=tk.Canvas(width=1000,height=750)          #canvas1(ホーム画面)の設定
canvas1.place(x=0,y=0)

selectionBtn = tk.Button(ColorHolder, text="Selection Color",
                       command=lambda:transition_button1(canvas1))  #セレクション画面に遷移するボタン           
selectionBtn.place(x=a*4.5, y=0.2*b)


webBtn = tk.Button(ColorHolder, text="Web Color",
                       command=lambda:transition_button3(canvas1))  #Web画面に遷移するボタン
webBtn.place(x=a*10, y=0.2*b)

WebEntry = tk.Entry(width = 35)                                     #URL入力エントリーボックス
WebEntry.insert(0,"http://www.shido.info/py/tkinter2.html")         #エントリーボックスの初期値設定
WebEntry.place(x=a*10, y=0.8*b)




#画面遷移ボタン(Sellection)の処理
def transition_button1(home):
    test=tk.Toplevel()
    home.place_forget()                                          #canvas1(home)を隠す
    canvas2 =tk.Canvas(background="#eca",width=500,height=400)   #セレクション画面の設定
    canvas2.place(x=a*4.5,y=0)
    returnBtn1 = tk.Button(ColorHolder, text="Back",
                       command=lambda:transition_button2(canvas2))
    returnBtn1.place(x=a*5.5, y=0.2*b)
    
#画面遷移ボタン(Back)の処理 
def transition_button2(palette):
    palette.place_forget()
    """
    returnBtn.destroy()                #「back」画面が消せない
    print("Backを消した！！！")        #NameError: name 'returnBtn' is not defined

    """


    
#画面遷移ボタン(Web)の処理
def transition_button3(home):
    home.place_forget()                                          #canvas1(home)を隠す
    canvas3 =tk.Canvas(background="#cea",width=500,height=400)   #Web画面の設定
    canvas3.place(x=a*10,y=0)
    returnBtn2 = tk.Button(ColorHolder, text="Back",
                       command=lambda:transition_button4(canvas3))
    returnBtn2.place(x=a*11, y=0.2*b)
    
#画面遷移ボタン(Back)の処理 
def transition_button4(palette):
    palette.place_forget()
    """
    returnBtn.destroy()                #「back」画面が消せない
    print("Backを消した！！！")        #NameError: name 'returnBtn' is not defined
    """



"""                             
def AddColor(color):         #カラーホルダーの生成（①ラジオボタン、②エントリーボックス、③ラベル）
    #ラジオボタン
    radio =tk.Radiobutton(ColorHolder, value=num, variable=var,text="color"+str(num+1))
    radioList.append(radio)   
   
    #エントリーボックス
    entry = tk.Entry(width = 13,background = '#ffffff',foreground = '#000000')
    entryList.append(entry)

    #ラベル
    label=tk.Label(width = 4,height = 2,relief = "groove",background =color)
    labelList.append(label)   
"""

def AddColor(color):         #カラーホルダーの生成（①ラジオボタン、②エントリーボックス、③ラベル）
    #ラジオボタン
    radio =tk.Radiobutton(ColorHolder, variable=var)
    radioList.append(radio)   
    radio.place
   
    #エントリーボックス
    entry = tk.Entry(width = 13,background = '#ffffff',foreground = '#000000')
    entryList.append(entry)

    #ラベル
    label=tk.Label(width = 4,height = 2,relief = "groove",background =color)
    labelList.append(label)

    num=radioList.length()
    
    
    AddColor(color)
    
    radioList[num].place(x=a,y=b*(1+num))
    entryList[num].place(x=a*1.8, y=b*(1+num))
    labelList[num].place(x=a*2.8, y=b*(1+num))
    
    Create_delBtn()
    delList[num].place(x=a*3.3, y=b*(1+num))    
    print(len(radioList))
    print(num)


   


#デフォルトで3色を設置
for num in range (3):
    AddColor(colorList[num])
    radioList[num].place(x=a,y=b*(1+num))
    entryList[num].place(x=a*1.8, y=b*(1+num))
    entryList[num].insert(1,colorList[num])
    labelList[num].place(x=a*2.8, y=b*(1+num))






#エンターキーを押したときに実行する処理
#       処理①ラベル3個の色をEntに入力されたカラーコードに変更する。
#       処理②プレビュー画面２つの色をEntに入力されたカラーコードに変更する。
#       処理③例外処理

#変数i:エンターキーが押されたエントリーボックスのインデックス番号

def colorChange0(event):
    try:
        labelList[0].config(bg= entryList[0].get())
        canvas1.configure(id0,fg = entryList[0].get())
  
        
    except tk.TclError:
        error=0

entryList[0].bind("<Return>",colorChange0)



"""
    canvasPreview.create_rectangle(0,0,450,450, fill=entryList[1].get())
    canvasPreview.create_rectangle(450,0,900,450, fill=entryList[2].get())




def colorChange(event):
    try:
        labelList[i].config(bg= entryList[i].get())
    except tkinter.TclError:
        error=0





#☆②イベントの処理の設定
#    エンターキーが押されたときにラベルの色を変更

#入力されたエントリーボックスのインデックス「i」を探す


for index in range (num+1):
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
def DelBtn_click():
    
    #delList
    radioList[2].destroy()  #delボタンが押されたところのnumのradioボタンを消す
    entryList[2].destroy()  #delボタンが押されたところの配列のindexを取得したい
    labelList[2].destroy()
    delList[2].destroy()
    
    radioList.pop()     #pop() 配列の要素を一つ消すメソッド
    entryList.pop()     #配列の数を減らすと、AddCollor()でradioList[num]が範囲外となる。
    labelList.pop()
    delList.pop()

    num -=1             #numもマイナス1する
                        #すでに設置済のカラーホルダーをなくなったところに移動させる必要がある。
                        #AddCollorをしても、すでに設置済みのものにかぶってしまうから。
                    
    
    print(len(radioList))
    print(num)
  
    


#カラーの個数分、削除ボタンを設置
def Create_delBtn():
    delBtn = tk.Button(ColorHolder, text="Delet", command=DelBtn_click)
    delList.append(delBtn)
    
print(len(radioList))
print(num)
    
for i in range(len(radioList)):
    Create_delBtn()
    delList[i].place(x=a*3.3, y=b*(1+i))

    
def AddColor(color):
    global num
    num += 1
    AddColor(color)
    
    radioList[num].place(x=a,y=b*(1+num))
    entryList[num].place(x=a*1.8, y=b*(1+num))
    labelList[num].place(x=a*2.8, y=b*(1+num))
    
    Create_delBtn()
    delList[num].place(x=a*3.3, y=b*(1+num))    
    print(len(radioList))
    print(num)





"""
#カラー追加ボタンで色を追加　　
def AddBtn_click():
    global num
    num += 1
    AddColor(color)
    
    radioList[num].place(x=a,y=b*(1+num))
    entryList[num].place(x=a*1.8, y=b*(1+num))
    labelList[num].place(x=a*2.8, y=b*(1+num))
    
    Create_delBtn()
    delList[num].place(x=a*3.3, y=b*(1+num))    
    print(len(radioList))
    print(num)
"""    
addBtn = tk.Button(ColorHolder, text="Add Color", command=AddBtn_click)           
addBtn.place(x=a*0.2, y=b*3.5)

print(len(radioList))
print(num)


id1=canvas1.create_rectangle(a,b*(2+num),a+450,b*(2+num)+450, fill=entryList[1].get())
id2=canvas1.create_rectangle(a+450,b*(2+num),a+900,b*(2+num)+450, fill=entryList[2].get())
id0=canvas1.create_text(a+450,b*(2+num)+220,text="Sample", fill= entryList[0].get(),
                     font=("MSゴシック", "80", "bold"))

"""
#プレビュー画面(ホーム画面canvas1に追加する)  
def Preview():
    id1=canvas1.create_rectangle(a,b*(2+num),a+450,b*(2+num)+450, fill=entryList[1].get())
    id2=canvas1.create_rectangle(a+450,b*(2+num),a+900,b*(2+num)+450, fill=entryList[2].get())
    id0=canvas1.create_text(a+450,b*(2+num)+220,text="Sample", fill= entryList[0].get(),
                     font=("MSゴシック", "80", "bold"))
    #canvas1.itemconfigure(id0,fill = "red")
#entryList[3].
Preview()
"""
#canvas1.itemconfigure(id0,fill = "orange")
canvas1.itemconfigure(id1,fill = "red")

    
ColorHolder.mainloop()

 
